import type { Layer, PickingInfo, Position } from '@deck.gl/core';
import { TripsLayer } from '@deck.gl/geo-layers';
import {
  ArcLayer,
  ColumnLayer,
  GeoJsonLayer,
  ScatterplotLayer,
  TextLayer,
} from '@deck.gl/layers';
import type { FeatureCollection, GeoJsonProperties, Geometry } from 'geojson';

import { averageResidual, classify, metricsFor } from '../model/classify';
import { centers, flows } from '../model/demo_data';
import type {
  CenterDatum,
  CenterMetrics,
  DiagnosisClass,
  FlowDatum,
  ScenarioId,
  Thresholds,
  ViewMode,
} from '../model/types';

export const classColors: Record<DiagnosisClass, [number, number, number]> = {
  borrowed: [39, 168, 150],
  shadow: [155, 85, 125],
  mixed: [230, 169, 72],
  independent: [22, 49, 57],
  'weak-periphery': [129, 145, 151],
  unresolved: [111, 122, 128],
};

const COLORS = {
  carbon: [22, 49, 57] as [number, number, number],
  coral: [240, 107, 79] as [number, number, number],
  teal: [39, 168, 150] as [number, number, number],
  plum: [155, 85, 125] as [number, number, number],
  steel: [129, 145, 151] as [number, number, number],
  mist: [230, 238, 235] as [number, number, number],
};

const ZERO_ALTITUDE = 5200;

interface RenderCenter {
  center: CenterDatum;
  metrics: CenterMetrics;
  baselineClass: DiagnosisClass;
  scenarioClass: DiagnosisClass;
  displayClass: DiagnosisClass;
  residual: number;
  height: number;
  baseAltitude: number;
  tooltip: string;
}

interface RenderFlow extends FlowDatum {
  source: CenterDatum;
  target: CenterDatum;
  path: Position[];
  timestamps: number[];
}

interface RobustnessRing {
  item: RenderCenter;
  index: number;
}

export interface BuildLayersOptions {
  boundaryData: FeatureCollection<Geometry, GeoJsonProperties> | null;
  mode: ViewMode;
  scenarioId: ScenarioId;
  thresholds: Thresholds;
  animationTime: number;
  selectedId: string;
  onSelect: (id: string) => void;
}

function curvePath(source: Position, target: Position): Position[] {
  const points: Position[] = [];
  const steps = 28;
  const dx = target[0] - source[0];
  const dy = target[1] - source[1];
  const distance = Math.sqrt(dx * dx + dy * dy);
  const side = distance * 0.11;
  const normalX = distance === 0 ? 0 : -dy / distance;
  const normalY = distance === 0 ? 0 : dx / distance;

  for (let i = 0; i <= steps; i += 1) {
    const t = i / steps;
    const bend = Math.sin(Math.PI * t) * side;
    points.push([
      source[0] + dx * t + normalX * bend,
      source[1] + dy * t + normalY * bend,
      900 + Math.sin(Math.PI * t) * 4300,
    ]);
  }

  return points;
}

function alpha(color: [number, number, number], opacity: number) {
  return [...color, Math.round(opacity)] as [number, number, number, number];
}

function renderCenters(
  mode: ViewMode,
  scenarioId: ScenarioId,
  thresholds: Thresholds,
): RenderCenter[] {
  return centers
    .filter((center) => !center.isCore)
    .map((center) => {
      const scenarioMetrics = metricsFor(center, scenarioId);
      const baselineClass = classify(center.baseline, thresholds);
      const scenarioClass = classify(scenarioMetrics, thresholds);
      const shownMetrics = mode === 'baseline' ? center.baseline : scenarioMetrics;
      const residual =
        mode === 'delta'
          ? averageResidual(scenarioMetrics) - averageResidual(center.baseline)
          : averageResidual(shownMetrics);
      const magnitude = 800 + Math.abs(residual) * 16500;
      const baseAltitude = residual >= 0 ? ZERO_ALTITUDE : ZERO_ALTITUDE - magnitude;
      const displayClass = mode === 'baseline' ? baselineClass : scenarioClass;

      return {
        center,
        metrics: shownMetrics,
        baselineClass,
        scenarioClass,
        displayClass,
        residual,
        height: magnitude,
        baseAltitude,
        tooltip: `${center.label} · ${center.anchor}`,
      };
    });
}

function renderFlows(mode: ViewMode, scenarioId: ScenarioId): RenderFlow[] {
  const factor = scenarioId === 'EV-OPEN' ? 0.78 : scenarioId === 'EV-FULL' ? 1.12 : 1;
  const visibleFactor = mode === 'baseline' ? 1 : factor;

  return flows.map((flow) => {
    const source = centers.find((center) => center.id === flow.sourceId)!;
    const target = centers.find((center) => center.id === flow.targetId)!;
    const path = curvePath(source.coordinates, target.coordinates);

    return {
      ...flow,
      strength: Math.min(1, flow.strength * visibleFactor),
      source,
      target,
      path,
      timestamps: path.map((_, index) => (index / (path.length - 1)) * 100),
    };
  });
}

export function buildLayers(options: BuildLayersOptions): Layer[] {
  const {
    boundaryData,
    mode,
    scenarioId,
    thresholds,
    animationTime,
    selectedId,
    onSelect,
  } = options;
  const items = renderCenters(mode, scenarioId, thresholds);
  const renderedFlows = renderFlows(mode, scenarioId);
  const core = centers.find((center) => center.isCore)!;
  const rings: RobustnessRing[] =
    mode === 'robustness'
      ? items.flatMap((item) => [0, 1, 2].map((index) => ({ item, index })))
      : [];

  const layers: Layer[] = [];

  if (boundaryData) {
    layers.push(
      new GeoJsonLayer({
        id: 'boundaries',
        data: boundaryData,
        pickable: false,
        stroked: true,
        filled: true,
        getFillColor: (feature) =>
          feature.properties?.role === 'dki-core'
            ? alpha(COLORS.coral, 34)
            : alpha(COLORS.mist, 24),
        getLineColor: (feature) =>
          feature.properties?.role === 'dki-core'
            ? alpha(COLORS.coral, 235)
            : alpha(COLORS.carbon, 72),
        getLineWidth: (feature) => (feature.properties?.role === 'dki-core' ? 3 : 1),
        lineWidthMinPixels: 1,
        lineWidthMaxPixels: 4,
        beforeId: 'label_village',
      }),
    );
  }

  layers.push(
    new ScatterplotLayer({
      id: 'burden-halos',
      data: items,
      pickable: false,
      getPosition: (item: RenderCenter) => [...item.center.coordinates, 60],
      getRadius: (item: RenderCenter) => 5200 + item.metrics.burden * 12800,
      radiusUnits: 'meters',
      filled: true,
      stroked: false,
      getFillColor: (item: RenderCenter) =>
        alpha(item.metrics.burden >= thresholds.burden ? COLORS.plum : COLORS.coral, 18 + item.metrics.burden * 28),
      beforeId: 'label_village',
    }),
  );

  layers.push(
    new ArcLayer({
      id: 'relational-arcs',
      data: renderedFlows,
      pickable: false,
      getSourcePosition: (flow: RenderFlow) => flow.source.coordinates,
      getTargetPosition: (flow: RenderFlow) => flow.target.coordinates,
      getSourceColor: (flow: RenderFlow) =>
        alpha(flow.relation === 'core-bound' ? COLORS.coral : COLORS.teal, mode === 'delta' ? 75 : 145),
      getTargetColor: (flow: RenderFlow) =>
        alpha(flow.relation === 'core-bound' ? COLORS.carbon : COLORS.teal, mode === 'delta' ? 60 : 110),
      getWidth: (flow: RenderFlow) => 1 + flow.strength * 4.2,
      widthUnits: 'pixels',
      greatCircle: false,
      beforeId: 'label_village',
    }),
  );

  layers.push(
    new TripsLayer({
      id: 'animated-flows',
      data: renderedFlows,
      pickable: false,
      getPath: (flow: RenderFlow) => flow.path,
      getTimestamps: (flow: RenderFlow) => flow.timestamps,
      getColor: (flow: RenderFlow) =>
        flow.relation === 'core-bound' ? alpha(COLORS.coral, 235) : alpha(COLORS.teal, 215),
      currentTime: animationTime,
      trailLength: 12,
      capRounded: true,
      jointRounded: true,
      widthMinPixels: 2,
      getWidth: (flow: RenderFlow) => 1.2 + flow.strength * 2.6,
      beforeId: 'label_village',
    }),
  );

  layers.push(
    new ScatterplotLayer({
      id: 'zero-datum-plates',
      data: items,
      pickable: true,
      stroked: true,
      filled: true,
      getPosition: (item: RenderCenter) => [...item.center.coordinates, ZERO_ALTITUDE],
      getRadius: (item: RenderCenter) => 3500 + item.metrics.robustness * 1800,
      radiusUnits: 'meters',
      getFillColor: alpha(COLORS.mist, 92),
      getLineColor: (item: RenderCenter) => alpha(classColors[item.displayClass], 225),
      getLineWidth: (item: RenderCenter) => (item.center.id === selectedId ? 4 : 2),
      lineWidthUnits: 'pixels',
      onClick: (info: PickingInfo<RenderCenter>) => {
        if (info.object) onSelect(info.object.center.id);
      },
      beforeId: 'label_village',
    }),
  );

  layers.push(
    new ColumnLayer({
      id: 'residual-columns',
      data: items,
      pickable: true,
      diskResolution: 40,
      radius: 2150,
      extruded: true,
      wireframe: false,
      getPosition: (item: RenderCenter) => [
        item.center.coordinates[0],
        item.center.coordinates[1],
        item.baseAltitude,
      ],
      getElevation: (item: RenderCenter) => item.height,
      getFillColor: (item: RenderCenter) =>
        alpha(item.residual >= 0 ? COLORS.teal : COLORS.plum, item.center.id === selectedId ? 245 : 205),
      getLineColor: alpha(COLORS.mist, 150),
      onClick: (info: PickingInfo<RenderCenter>) => {
        if (info.object) onSelect(info.object.center.id);
      },
      material: {
        ambient: 0.62,
        diffuse: 0.7,
        shininess: 18,
        specularColor: [215, 234, 228],
      },
      beforeId: 'label_village',
    }),
  );

  if (rings.length > 0) {
    layers.push(
      new ScatterplotLayer({
        id: 'robustness-rings',
        data: rings,
        pickable: false,
        stroked: true,
        filled: false,
        getPosition: (ring: RobustnessRing) => [
          ...ring.item.center.coordinates,
          ZERO_ALTITUDE + ring.index * 130,
        ],
        getRadius: (ring: RobustnessRing) =>
          5000 + ring.index * 1850 + (1 - ring.item.metrics.robustness) * 4200,
        radiusUnits: 'meters',
        getLineColor: (ring: RobustnessRing) =>
          alpha(COLORS.steel, Math.max(35, 145 - ring.index * 35)),
        getLineWidth: 1.5,
        lineWidthUnits: 'pixels',
        beforeId: 'label_village',
      }),
    );
  }

  layers.push(
    new ScatterplotLayer({
      id: 'jakarta-core',
      data: [core],
      pickable: false,
      getPosition: (center: CenterDatum) => [...center.coordinates, 120],
      getRadius: 9100,
      radiusUnits: 'meters',
      filled: true,
      stroked: true,
      getFillColor: alpha(COLORS.coral, 215),
      getLineColor: alpha(COLORS.mist, 245),
      getLineWidth: 3,
      lineWidthUnits: 'pixels',
      beforeId: 'label_village',
    }),
  );

  layers.push(
    new TextLayer({
      id: 'center-labels',
      data: [...items, { center: core, height: 0, residual: 0 }],
      pickable: false,
      billboard: true,
      getPosition: (item: Partial<RenderCenter> & { center: CenterDatum }) => {
        if (item.center.isCore) return [...item.center.coordinates, 1500];
        const altitude =
          item.residual && item.residual > 0
            ? ZERO_ALTITUDE + (item.height ?? 0) + 900
            : ZERO_ALTITUDE + 900;
        return [...item.center.coordinates, altitude];
      },
      getText: (item: Partial<RenderCenter> & { center: CenterDatum }) =>
        item.center.isCore ? 'JAKARTA / INTI TETAP' : item.center.label,
      getColor: (item: Partial<RenderCenter> & { center: CenterDatum }) =>
        item.center.isCore ? alpha(COLORS.coral, 255) : alpha(COLORS.carbon, 235),
      getSize: (item: Partial<RenderCenter> & { center: CenterDatum }) =>
        item.center.isCore ? 16 : 13,
      sizeUnits: 'pixels',
      fontFamily: 'Saira Semi Condensed',
      fontWeight: 600,
      fontSettings: { sdf: true, radius: 8, cutoff: 0.25 },
      outlineWidth: 3,
      outlineColor: alpha(COLORS.mist, 235),
      getTextAnchor: 'middle',
      getAlignmentBaseline: 'bottom',
      beforeId: 'label_village',
    }),
  );

  return layers;
}
