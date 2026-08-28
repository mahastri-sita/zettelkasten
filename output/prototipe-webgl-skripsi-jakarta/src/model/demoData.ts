import type {
  CenterDatum,
  EvidenceModule,
  FlowDatum,
  MetricAdjustment,
  Provenance,
  Scenario,
  ScenarioId,
  Thresholds,
} from './types';

const adjustment = (
  integration: number,
  serviceResidual: number,
  jobResidual: number,
  benefit: number,
  burden: number,
  robustness: number,
): MetricAdjustment => ({
  integration,
  serviceResidual,
  jobResidual,
  benefit,
  burden,
  robustness,
});

const commonAdjustments: Record<ScenarioId, MetricAdjustment> = {
  'EV-OPEN': adjustment(-0.1, -0.06, -0.08, -0.08, 0.05, -0.16),
  'EV-MIN': adjustment(0, 0, 0, 0, 0, 0),
  'EV-FULL': adjustment(0.07, 0.05, 0.08, 0.06, -0.04, 0.12),
};

export const defaultThresholds: Thresholds = {
  integration: 0.6,
  residual: 0.15,
  burden: 0.55,
  robustness: 0.65,
};

export const provenance: Provenance = {
  demo: true,
  year: '2024',
  unit: 'titik ilustratif',
  disclaimer: 'Ilustrasi prototipe — bukan hasil penelitian.',
  geometryUse:
    'Batas wilayah hanya konteks kartografis; titik A–F bukan delineasi pusat sekunder final.',
};

export const centers: CenterDatum[] = [
  {
    id: 'jakarta-core',
    label: 'Jakarta',
    anchor: 'inti tetap',
    coordinates: [106.8272, -6.1754],
    isCore: true,
    baseline: {
      integration: 1,
      serviceResidual: 0,
      jobResidual: 0,
      benefit: 1,
      burden: 0.35,
      robustness: 1,
    },
    adjustments: {
      'EV-OPEN': adjustment(0, 0, 0, 0, 0, 0),
      'EV-MIN': adjustment(0, 0, 0, 0, 0, 0),
      'EV-FULL': adjustment(0, 0, 0, 0, 0, 0),
    },
  },
  {
    id: 'center-a',
    label: 'Pusat A',
    anchor: 'titik demo koridor barat',
    coordinates: [106.6319, -6.1783],
    baseline: {
      integration: 0.78,
      serviceResidual: 0.25,
      jobResidual: 0.34,
      benefit: 0.72,
      burden: 0.4,
      robustness: 0.82,
    },
    adjustments: commonAdjustments,
  },
  {
    id: 'center-b',
    label: 'Pusat B',
    anchor: 'titik demo koridor barat daya',
    coordinates: [106.718, -6.288],
    baseline: {
      integration: 0.67,
      serviceResidual: 0.22,
      jobResidual: -0.18,
      benefit: 0.66,
      burden: 0.72,
      robustness: 0.73,
    },
    adjustments: {
      ...commonAdjustments,
      'EV-FULL': adjustment(0.08, 0.03, 0.11, 0.05, -0.08, 0.16),
    },
  },
  {
    id: 'center-c',
    label: 'Pusat C',
    anchor: 'titik demo koridor selatan',
    coordinates: [106.818, -6.402],
    baseline: {
      integration: 0.74,
      serviceResidual: -0.24,
      jobResidual: -0.19,
      benefit: 0.48,
      burden: 0.76,
      robustness: 0.78,
    },
    adjustments: {
      ...commonAdjustments,
      'EV-FULL': adjustment(0.06, 0.08, 0.09, 0.08, -0.08, 0.1),
    },
  },
  {
    id: 'center-d',
    label: 'Pusat D',
    anchor: 'titik demo koridor selatan jauh',
    coordinates: [106.793, -6.595],
    baseline: {
      integration: 0.47,
      serviceResidual: 0.12,
      jobResidual: 0.18,
      benefit: 0.58,
      burden: 0.33,
      robustness: 0.8,
    },
    adjustments: commonAdjustments,
  },
  {
    id: 'center-e',
    label: 'Pusat E',
    anchor: 'titik demo koridor timur',
    coordinates: [106.995, -6.238],
    baseline: {
      integration: 0.55,
      serviceResidual: -0.28,
      jobResidual: -0.2,
      benefit: 0.35,
      burden: 0.62,
      robustness: 0.74,
    },
    adjustments: {
      ...commonAdjustments,
      'EV-FULL': adjustment(0.1, 0.1, 0.11, 0.08, -0.05, 0.14),
    },
  },
  {
    id: 'center-f',
    label: 'Pusat F',
    anchor: 'titik demo koridor industri timur',
    coordinates: [107.145, -6.306],
    baseline: {
      integration: 0.64,
      serviceResidual: 0.08,
      jobResidual: 0.19,
      benefit: 0.66,
      burden: 0.58,
      robustness: 0.59,
    },
    adjustments: {
      ...commonAdjustments,
      'EV-FULL': adjustment(0.09, 0.08, 0.1, 0.07, -0.04, 0.19),
    },
  },
];

export const flows: FlowDatum[] = [
  { id: 'a-core', sourceId: 'center-a', targetId: 'jakarta-core', strength: 0.82, burden: 0.44, relation: 'core-bound' },
  { id: 'b-core', sourceId: 'center-b', targetId: 'jakarta-core', strength: 0.69, burden: 0.72, relation: 'core-bound' },
  { id: 'c-core', sourceId: 'center-c', targetId: 'jakarta-core', strength: 0.77, burden: 0.78, relation: 'core-bound' },
  { id: 'd-core', sourceId: 'center-d', targetId: 'jakarta-core', strength: 0.48, burden: 0.51, relation: 'core-bound' },
  { id: 'e-core', sourceId: 'center-e', targetId: 'jakarta-core', strength: 0.66, burden: 0.63, relation: 'core-bound' },
  { id: 'f-core', sourceId: 'center-f', targetId: 'jakarta-core', strength: 0.59, burden: 0.6, relation: 'core-bound' },
  { id: 'a-b', sourceId: 'center-a', targetId: 'center-b', strength: 0.46, burden: 0.35, relation: 'cross-center' },
  { id: 'b-c', sourceId: 'center-b', targetId: 'center-c', strength: 0.41, burden: 0.44, relation: 'cross-center' },
  { id: 'c-d', sourceId: 'center-c', targetId: 'center-d', strength: 0.38, burden: 0.49, relation: 'cross-center' },
  { id: 'c-e', sourceId: 'center-c', targetId: 'center-e', strength: 0.42, burden: 0.48, relation: 'cross-center' },
  { id: 'e-f', sourceId: 'center-e', targetId: 'center-f', strength: 0.55, burden: 0.39, relation: 'cross-center' },
  { id: 'b-e', sourceId: 'center-b', targetId: 'center-e', strength: 0.29, burden: 0.42, relation: 'cross-center' },
];

export const evidenceModules: EvidenceModule[] = [
  { code: 'F', label: 'Arus', year: '2023/24', unit: 'OD / orientasi', note: 'Bukti relasional atau potensi interaksi.' },
  { code: 'Jb', label: 'Pekerjaan', year: '2024', unit: 'lokasi kerja', note: 'Jumlah dan sektor pekerjaan pada unit sah.' },
  { code: 'L', label: 'Layanan lokal', year: '2024', unit: 'kehadiran', note: 'Kehadiran layanan bukan produktivitas.' },
  { code: 'E', label: 'Usaha', year: '2024', unit: 'titik/agregat', note: 'Kehadiran usaha dan fungsi keputusan dibedakan.' },
  { code: 'R', label: 'Kinerja', year: '2024', unit: 'agregat', note: 'Output, upah, dan produktivitas tidak diturunkan semu.' },
  { code: 'N', label: 'Jaringan', year: '2024', unit: 'ruas/waktu', note: 'Aksesibilitas potensial bukan arus aktual.' },
  { code: 'H', label: 'Layanan tinggi', year: '2024', unit: 'titik', note: 'Kelas dan kapasitas harus diverifikasi.' },
  { code: 'I', label: 'Industri', year: '2024', unit: 'kawasan', note: 'Poligon industri tidak membuktikan pekerjaan.' },
  { code: 'K', label: 'Lahan/perumahan', year: '2024', unit: 'zona', note: 'Konteks lokal dan beban tempat tinggal.' },
  { code: 'T', label: 'Temporal', year: 'lintas tahun', unit: 'seri', note: 'Status quo tidak disebut perubahan tanpa seri harmonis.' },
  { code: 'Gv', label: 'Batas/tanggung jawab', year: 'tetap', unit: 'administrasi', note: 'Jejak fungsional bukan perluasan yurisdiksi.' },
];

export const scenarios: Scenario[] = [
  {
    id: 'EV-OPEN',
    label: 'Baseline terbuka',
    levelM: 'M1',
    levelU: 'U1',
    description: 'Aksesibilitas dan fungsi proksi untuk pemetaan awal.',
    allowedClaim: 'Profil aksesibilitas–fungsi; tidak menghasilkan diagnosis relasional ketat.',
    evidence: { F: 'S', Jb: 'A', L: 'P', E: 'P', R: 'A', N: 'D', H: 'P', I: 'P', K: 'P', T: 'excluded', Gv: 'D' },
  },
  {
    id: 'EV-MIN',
    label: 'Desain minimum',
    levelM: 'M2',
    levelU: 'U2',
    description: 'Orientasi terarah dan satu dimensi fungsi langsung.',
    allowedClaim: 'Pola deskriptif-relasional yang konsisten pada konstruk yang terukur.',
    evidence: { F: 'A', Jb: 'A', L: 'D', E: 'P', R: 'A', N: 'D', H: 'D', I: 'P', K: 'P', T: 'excluded', Gv: 'D' },
  },
  {
    id: 'EV-FULL',
    label: 'Penguatan penuh',
    levelM: 'M3',
    levelU: 'U3',
    description: 'OD rinci serta pekerjaan dan layanan yang kompatibel.',
    allowedClaim: 'Kandidat diagnosis relasional setelah seluruh gerbang bukti lolos.',
    evidence: { F: 'D', Jb: 'D', L: 'D', E: 'A', R: 'A', N: 'D', H: 'D', I: 'A', K: 'A', T: 'S', Gv: 'D' },
  },
];

export const classLabels = {
  borrowed: 'Borrowed size',
  shadow: 'Agglomeration shadow',
  mixed: 'Campuran / transisional',
  independent: 'Relatif independen',
  'weak-periphery': 'Periferi lemah',
  unresolved: 'Tidak terselesaikan',
} as const;

export const gates = [
  'Bukti relasional terhadap Jakarta tersedia.',
  'Benchmark fungsi mengukur konstruk substantif.',
  'Unit, catchment, dan periode dapat dipadankan.',
  'Label bertahan pada uji sensitivitas utama.',
];
