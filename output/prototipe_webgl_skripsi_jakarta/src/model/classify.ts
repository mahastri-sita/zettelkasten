import type {
  CenterDatum,
  CenterMetrics,
  DiagnosisClass,
  ScenarioId,
  Thresholds,
} from './types';

const clamp01 = (value: number) => Math.max(0, Math.min(1, value));
const clampResidual = (value: number) => Math.max(-0.65, Math.min(0.65, value));

export function metricsFor(center: CenterDatum, scenarioId: ScenarioId): CenterMetrics {
  const adjustment = center.adjustments[scenarioId];

  return {
    integration: clamp01(center.baseline.integration + adjustment.integration),
    serviceResidual: clampResidual(
      center.baseline.serviceResidual + adjustment.serviceResidual,
    ),
    jobResidual: clampResidual(center.baseline.jobResidual + adjustment.jobResidual),
    benefit: clamp01(center.baseline.benefit + adjustment.benefit),
    burden: clamp01(center.baseline.burden + adjustment.burden),
    robustness: clamp01(center.baseline.robustness + adjustment.robustness),
  };
}

export function averageResidual(metrics: CenterMetrics) {
  return (metrics.serviceResidual + metrics.jobResidual) / 2;
}

export function classify(metrics: CenterMetrics, thresholds: Thresholds): DiagnosisClass {
  const residual = averageResidual(metrics);
  const opposingResiduals =
    metrics.serviceResidual >= thresholds.residual &&
    metrics.jobResidual <= -thresholds.residual;
  const opposingResidualsReverse =
    metrics.jobResidual >= thresholds.residual &&
    metrics.serviceResidual <= -thresholds.residual;

  if (metrics.robustness < thresholds.robustness) return 'unresolved';

  if (
    opposingResiduals ||
    opposingResidualsReverse ||
    (metrics.benefit >= thresholds.burden && metrics.burden >= thresholds.burden)
  ) {
    return 'mixed';
  }

  if (metrics.integration >= thresholds.integration && residual >= thresholds.residual) {
    return 'borrowed';
  }

  if (metrics.integration >= thresholds.integration && residual <= -thresholds.residual) {
    return 'shadow';
  }

  if (metrics.integration < thresholds.integration && residual >= -thresholds.residual) {
    return 'independent';
  }

  if (metrics.integration < thresholds.integration && residual < -thresholds.residual) {
    return 'weak-periphery';
  }

  return 'mixed';
}

export function displayMetrics(
  center: CenterDatum,
  scenarioId: ScenarioId,
  mode: 'baseline' | 'scenario' | 'delta' | 'robustness',
): CenterMetrics {
  const baseline = center.baseline;
  const scenario = metricsFor(center, scenarioId);

  if (mode === 'baseline') return baseline;
  if (mode === 'scenario' || mode === 'robustness') return scenario;

  return {
    integration: scenario.integration - baseline.integration,
    serviceResidual: scenario.serviceResidual - baseline.serviceResidual,
    jobResidual: scenario.jobResidual - baseline.jobResidual,
    benefit: scenario.benefit - baseline.benefit,
    burden: scenario.burden - baseline.burden,
    robustness: scenario.robustness - baseline.robustness,
  };
}
