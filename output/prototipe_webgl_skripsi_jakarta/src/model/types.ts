export type ViewMode = 'baseline' | 'scenario' | 'delta' | 'robustness';

export type ScenarioId = 'EV-OPEN' | 'EV-MIN' | 'EV-FULL';

export type EvidenceStatus = 'D' | 'A' | 'S' | 'P' | 'excluded';

export type DiagnosisClass =
  | 'borrowed'
  | 'shadow'
  | 'mixed'
  | 'independent'
  | 'weak-periphery'
  | 'unresolved';

export type ModuleCode =
  | 'F'
  | 'Jb'
  | 'L'
  | 'E'
  | 'R'
  | 'N'
  | 'H'
  | 'I'
  | 'K'
  | 'T'
  | 'Gv';

export interface Thresholds {
  integration: number;
  residual: number;
  burden: number;
  robustness: number;
}

export interface CenterMetrics {
  integration: number;
  serviceResidual: number;
  jobResidual: number;
  benefit: number;
  burden: number;
  robustness: number;
}

export interface MetricAdjustment {
  integration: number;
  serviceResidual: number;
  jobResidual: number;
  benefit: number;
  burden: number;
  robustness: number;
}

export interface CenterDatum {
  id: string;
  label: string;
  anchor: string;
  coordinates: [number, number];
  isCore?: boolean;
  baseline: CenterMetrics;
  adjustments: Record<ScenarioId, MetricAdjustment>;
}

export interface FlowDatum {
  id: string;
  sourceId: string;
  targetId: string;
  strength: number;
  burden: number;
  relation: 'core-bound' | 'cross-center';
}

export interface EvidenceModule {
  code: ModuleCode;
  label: string;
  year: string;
  unit: string;
  note: string;
}

export interface Scenario {
  id: ScenarioId;
  label: string;
  levelM: 'M1' | 'M2' | 'M3';
  levelU: 'U1' | 'U2' | 'U3';
  description: string;
  allowedClaim: string;
  evidence: Record<ModuleCode, EvidenceStatus>;
}

export interface Provenance {
  demo: true;
  year: '2024';
  unit: 'titik ilustratif';
  disclaimer: string;
  geometryUse: string;
}
