import type { FeatureCollection, GeoJsonProperties, Geometry } from 'geojson';
import {
  Activity,
  Database,
  Info,
  Layers3,
  RotateCcw,
  ShieldCheck,
  SlidersHorizontal,
  WifiOff,
  X,
} from 'lucide-react';
import { useCallback, useEffect, useMemo, useRef, useState, type CSSProperties } from 'react';
import Map, { AttributionControl, type MapRef } from 'react-map-gl/maplibre';

import { averageResidual, classify, metricsFor } from './model/classify';
import {
  centers,
  classLabels,
  defaultThresholds,
  evidenceModules,
  gates,
  provenance,
  scenarios,
} from './model/demoData';
import type {
  CenterMetrics,
  DiagnosisClass,
  EvidenceStatus,
  ScenarioId,
  Thresholds,
  ViewMode,
} from './model/types';
import { DeckOverlay } from './map/DeckOverlay';
import { buildLayers, classColors } from './map/layers';

const INITIAL_VIEW = {
  longitude: 106.84,
  latitude: -6.34,
  zoom: 9.02,
  pitch: 54,
  bearing: -16,
};

const MODE_LABELS: Record<ViewMode, string> = {
  baseline: 'Garis dasar',
  scenario: 'Skenario',
  delta: 'Selisih',
  robustness: 'Ketahanan',
};

const CLASS_COPY: Record<DiagnosisClass, string> = {
  borrowed:
    'Integrasi tinggi terbaca bersama surplus fungsi relatif. Label ini tetap kategori kerja.',
  shadow:
    'Integrasi tinggi terbaca bersama defisit fungsi relatif. Hubungan kausal tidak disimpulkan.',
  mixed:
    'Manfaat, beban, atau residual antardimensi bergerak ke arah yang berbeda.',
  independent:
    'Hubungan ke inti lebih rendah sementara fungsi lokal tidak menunjukkan defisit berarti.',
  'weak-periphery':
    'Hubungan metropolitan dan fungsi lokal sama-sama rendah dalam konfigurasi demo.',
  unresolved:
    'Kelas belum cukup stabil untuk diringkas; ketidakpastian dipertahankan sebagai hasil.',
};

const STATUS_LABELS: Record<EvidenceStatus, string> = {
  D: 'Langsung',
  A: 'Agregat',
  S: 'Sintetis',
  P: 'Proksi',
  excluded: 'Dikeluarkan',
};

type Drawer = 'sensitivity' | 'evidence' | null;

function hasWebGL() {
  try {
    const canvas = document.createElement('canvas');
    return Boolean(canvas.getContext('webgl2') || canvas.getContext('webgl'));
  } catch {
    return false;
  }
}

function useAnimationClock() {
  const [time, setTime] = useState(0);

  useEffect(() => {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let frame = 0;
    let last = 0;

    const tick = (now: number) => {
      if (!reduceMotion.matches && !document.hidden && now - last > 34) {
        setTime((now / 42) % 100);
        last = now;
      }
      frame = window.requestAnimationFrame(tick);
    };

    frame = window.requestAnimationFrame(tick);
    return () => window.cancelAnimationFrame(frame);
  }, []);

  return time;
}

function colorCss(classification: DiagnosisClass) {
  const [r, g, b] = classColors[classification];
  return `rgb(${r} ${g} ${b})`;
}

function valueLabel(value: number, residual = false) {
  if (residual) return `${value >= 0 ? '+' : ''}${value.toFixed(2)}`;
  return `${Math.round(value * 100)}%`;
}

function MetricRow({
  label,
  value,
  residual = false,
  delta = false,
}: {
  label: string;
  value: number;
  residual?: boolean;
  delta?: boolean;
}) {
  const normalized = residual ? Math.min(1, Math.abs(value) / 0.5) : Math.min(1, Math.abs(value));
  const tone = residual || delta ? (value >= 0 ? 'positive' : 'negative') : 'neutral';

  return (
    <div className="metric-row">
      <div className="metric-heading">
        <span>{label}</span>
        <strong>{valueLabel(value, residual || delta)}</strong>
      </div>
      <div className="metric-track" aria-hidden="true">
        <span
          className={`metric-fill metric-fill--${tone}`}
          style={{ width: `${Math.max(5, normalized * 100)}%` }}
        />
      </div>
    </div>
  );
}

function StaticFallback() {
  return (
    <main className="fallback-screen">
      <div className="fallback-visual" aria-hidden="true">
        <svg viewBox="0 0 900 560" role="img">
          <path d="M180 310 C310 170 470 160 690 260" />
          <path d="M220 390 C410 410 520 310 690 260" />
          <path d="M440 470 C470 370 540 320 690 260" />
          <circle className="fallback-core" cx="690" cy="260" r="28" />
          <circle cx="180" cy="310" r="14" />
          <circle cx="220" cy="390" r="14" />
          <circle cx="440" cy="470" r="14" />
          <circle cx="470" cy="165" r="14" />
        </svg>
      </div>
      <section className="fallback-card">
        <span className="eyebrow">Fallback visual</span>
        <h1>WebGL tidak tersedia di browser ini.</h1>
        <p>
          Aktifkan hardware acceleration atau buka prototipe di Chrome terbaru. Substansi demo tetap
          merupakan ilustrasi, bukan hasil penelitian.
        </p>
      </section>
    </main>
  );
}

export default function App() {
  const mapRef = useRef<MapRef>(null);
  const tileErrors = useRef(0);
  const [webglAvailable] = useState(hasWebGL);
  const [boundaryData, setBoundaryData] = useState<FeatureCollection<Geometry, GeoJsonProperties> | null>(null);
  const [mode, setMode] = useState<ViewMode>('baseline');
  const [scenarioId, setScenarioId] = useState<ScenarioId>('EV-MIN');
  const [selectedId, setSelectedId] = useState('center-a');
  const [thresholds, setThresholds] = useState<Thresholds>(defaultThresholds);
  const [drawer, setDrawer] = useState<Drawer>(null);
  const [mapLoaded, setMapLoaded] = useState(false);
  const [networkWarning, setNetworkWarning] = useState(false);
  const animationTime = useAnimationClock();

  const selectedScenario = scenarios.find((scenario) => scenario.id === scenarioId)!;
  const selectedCenter = centers.find((center) => center.id === selectedId)!;
  const scenarioMetrics = metricsFor(selectedCenter, scenarioId);
  const baselineClass = classify(selectedCenter.baseline, thresholds);
  const scenarioClass = classify(scenarioMetrics, thresholds);
  const selectedClass = mode === 'baseline' ? baselineClass : scenarioClass;
  const shownMetrics: CenterMetrics =
    mode === 'baseline'
      ? selectedCenter.baseline
      : mode === 'delta'
        ? {
            integration: scenarioMetrics.integration - selectedCenter.baseline.integration,
            serviceResidual:
              scenarioMetrics.serviceResidual - selectedCenter.baseline.serviceResidual,
            jobResidual: scenarioMetrics.jobResidual - selectedCenter.baseline.jobResidual,
            benefit: scenarioMetrics.benefit - selectedCenter.baseline.benefit,
            burden: scenarioMetrics.burden - selectedCenter.baseline.burden,
            robustness: scenarioMetrics.robustness - selectedCenter.baseline.robustness,
          }
        : scenarioMetrics;

  useEffect(() => {
    const controller = new AbortController();
    const base = import.meta.env.BASE_URL;

    fetch(`${base}data/jabodetabek-boundaries.geojson`, { signal: controller.signal })
      .then((response) => {
        if (!response.ok) throw new Error('Batas lokal tidak dapat dibaca.');
        return response.json();
      })
      .then((data: FeatureCollection<Geometry, GeoJsonProperties>) => setBoundaryData(data))
      .catch((error: Error) => {
        if (error.name !== 'AbortError') setNetworkWarning(true);
      });

    return () => controller.abort();
  }, []);

  useEffect(() => {
    if (!mapLoaded) return;

    const timeout = window.setTimeout(() => {
      const map = mapRef.current?.getMap();
      if (map && !map.areTilesLoaded()) setNetworkWarning(true);
    }, 3500);

    return () => window.clearTimeout(timeout);
  }, [mapLoaded]);

  const resetCamera = useCallback(() => {
    mapRef.current?.flyTo({ ...INITIAL_VIEW, duration: 1200, essential: true });
  }, []);

  useEffect(() => {
    const handleKey = (event: KeyboardEvent) => {
      const target = event.target as HTMLElement | null;
      if (event.key === 'Escape') {
        setDrawer(null);
        return;
      }
      if (target?.matches('input, select, textarea')) return;

      if (event.key === '1') setMode('baseline');
      if (event.key === '2') setMode('scenario');
      if (event.key === '3') setMode('delta');
      if (event.key === '4') setMode('robustness');
      if (event.key.toLowerCase() === 'r') resetCamera();
    };

    window.addEventListener('keydown', handleKey);
    return () => window.removeEventListener('keydown', handleKey);
  }, [resetCamera]);

  const layers = useMemo(
    () =>
      buildLayers({
        boundaryData,
        mode,
        scenarioId,
        thresholds,
        animationTime,
        selectedId,
        onSelect: setSelectedId,
      }),
    [boundaryData, mode, scenarioId, thresholds, animationTime, selectedId],
  );

  const updateThreshold = (key: keyof Thresholds, value: number) => {
    setThresholds((current) => ({ ...current, [key]: value }));
  };

  if (!webglAvailable) return <StaticFallback />;

  return (
    <main className={`app-shell${drawer ? ' app-shell--drawer-open' : ''}`}>
      <a className="skip-link" href="#controls">
        Lewati peta
      </a>

      <section className="map-stage" aria-label="Peta WebGL Medan Relasional Jakarta">
        <Map
          ref={mapRef}
          initialViewState={INITIAL_VIEW}
          mapStyle={`${import.meta.env.BASE_URL}map-style.json`}
          minZoom={7.1}
          maxZoom={12}
          maxPitch={68}
          cooperativeGestures={false}
          attributionControl={false}
          onLoad={(event) => {
            event.target.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
            setMapLoaded(true);
          }}
          onError={(event) => {
            const message = String(event.error?.message ?? '');
            if (/fetch|network|tile|source/i.test(message)) {
              tileErrors.current += 1;
              setNetworkWarning(true);
            }
          }}
          onIdle={() => {
            const map = mapRef.current?.getMap();
            if (map?.areTilesLoaded() && tileErrors.current === 0) setNetworkWarning(false);
          }}
        >
          <DeckOverlay
            interleaved
            layers={layers}
            useDevicePixels={1.5}
            getTooltip={({ object }) =>
              object?.tooltip
                ? {
                    html: `<strong>${object.center.label}</strong><br/><span>${object.center.anchor}</span><br/><small>Data sintetis untuk prototipe</small>`,
                    className: 'map-tooltip',
                  }
                : null
            }
          />
          <AttributionControl compact position="bottom-right" />
        </Map>
      </section>

      {!mapLoaded && (
        <div className="map-loader" role="status">
          <span />
          Menyiapkan medan relasional
        </div>
      )}

      {networkWarning && (
        <div className="network-notice" role="status">
          <WifiOff size={15} />
          Basemap daring terbatas. Layer prototipe tetap berjalan.
        </div>
      )}

      <header className="title-card glass-panel">
        <div className="title-card__meta">
          <span className="eyebrow">Eksperimen spasial · Skripsi 2026</span>
          <span className="live-mark"><i /> WebGL</span>
        </div>
        <h1>Medan Relasional<br />Jakarta</h1>
        <p className="title-card__thesis">
          Dekat bukan berarti diuntungkan. Keterhubungan dapat memperbesar fungsi lokal—atau
          menaunginya.
        </p>
        <div className="disclaimer-ribbon">
          <Info size={14} />
          <span>{provenance.disclaimer}</span>
        </div>
      </header>

      <section className="status-rail glass-panel" aria-label="Konfigurasi bukti">
        <div className="status-rail__fixed">
          <span>Simulasi bukti</span>
          <strong>{selectedScenario.levelM} / {selectedScenario.levelU}</strong>
          <span>{provenance.year} · {provenance.unit}</span>
        </div>
        <div className="scenario-switch" role="radiogroup" aria-label="Pilih skenario bukti simulasi">
          {scenarios.map((scenario) => (
            <button
              key={scenario.id}
              type="button"
              role="radio"
              aria-checked={scenarioId === scenario.id}
              className={scenarioId === scenario.id ? 'is-active' : ''}
              onClick={() => {
                setScenarioId(scenario.id);
                if (mode === 'baseline') setMode('scenario');
              }}
            >
              {scenario.id}
            </button>
          ))}
        </div>
      </section>

      <aside className="profile-panel glass-panel" aria-live="polite">
        <div className="profile-panel__head">
          <div>
            <span className="eyebrow">Titik ilustratif · {selectedCenter.label}</span>
            <h2>{selectedCenter.anchor}</h2>
          </div>
          <Activity size={19} />
        </div>

        <div
          className="class-chip"
          style={{ '--class-color': colorCss(selectedClass) } as CSSProperties}
        >
          <span />
          {mode === 'delta'
            ? `${classLabels[baselineClass]} → ${classLabels[scenarioClass]}`
            : classLabels[selectedClass]}
        </div>
        <p className="class-copy">{CLASS_COPY[selectedClass]}</p>

        <div className="metric-list">
          <MetricRow label="Integrasi" value={shownMetrics.integration} delta={mode === 'delta'} />
          <MetricRow label="Residual layanan" value={shownMetrics.serviceResidual} residual />
          <MetricRow label="Residual pekerjaan" value={shownMetrics.jobResidual} residual />
          <MetricRow label="Manfaat" value={shownMetrics.benefit} delta={mode === 'delta'} />
          <MetricRow label="Beban" value={shownMetrics.burden} delta={mode === 'delta'} />
          <MetricRow label="Ketahanan" value={shownMetrics.robustness} delta={mode === 'delta'} />
        </div>

        <div className="profile-panel__foot">
          <span>R̄ {valueLabel(averageResidual(mode === 'baseline' ? selectedCenter.baseline : scenarioMetrics), true)}</span>
          <span>Mode · {MODE_LABELS[mode]}</span>
        </div>
      </aside>

      <aside className="legend glass-panel" aria-label="Legenda kelas kerja">
        <span className="eyebrow">Kategori kerja</span>
        <div className="legend__items">
          {(Object.keys(classLabels) as DiagnosisClass[]).map((key) => (
            <div key={key}>
              <i style={{ background: colorCss(key) }} />
              <span>{classLabels[key]}</span>
            </div>
          ))}
        </div>
      </aside>

      <nav className="control-dock glass-panel" id="controls" aria-label="Kontrol presentasi">
        <div className="mode-switch" role="radiogroup" aria-label="Mode peta">
          {(Object.keys(MODE_LABELS) as ViewMode[]).map((item, index) => (
            <button
              key={item}
              type="button"
              role="radio"
              aria-checked={mode === item}
              className={mode === item ? 'is-active' : ''}
              onClick={() => setMode(item)}
            >
              <kbd>{index + 1}</kbd>
              {MODE_LABELS[item]}
            </button>
          ))}
        </div>
        <span className="control-divider" />
        <button
          type="button"
          className={drawer === 'sensitivity' ? 'is-active' : ''}
          aria-expanded={drawer === 'sensitivity'}
          onClick={() => setDrawer(drawer === 'sensitivity' ? null : 'sensitivity')}
        >
          <SlidersHorizontal size={16} />
          Sensitivitas
        </button>
        <button
          type="button"
          className={drawer === 'evidence' ? 'is-active' : ''}
          aria-expanded={drawer === 'evidence'}
          onClick={() => setDrawer(drawer === 'evidence' ? null : 'evidence')}
        >
          <Database size={16} />
          Bukti
        </button>
        <button type="button" title="Reset kamera (R)" onClick={resetCamera}>
          <RotateCcw size={16} />
          <span className="desktop-only">Reset</span>
        </button>
      </nav>

      {drawer && (
        <section className="drawer glass-panel" aria-label={drawer === 'sensitivity' ? 'Uji sensitivitas' : 'Ledger bukti'}>
          <div className="drawer__head">
            <div>
              <span className="eyebrow">{drawer === 'sensitivity' ? 'Parameter P-*' : 'Manifest bukti simulasi'}</span>
              <h2>{drawer === 'sensitivity' ? 'Uji ketahanan kelas' : selectedScenario.label}</h2>
            </div>
            <button type="button" aria-label="Tutup panel" onClick={() => setDrawer(null)}>
              <X size={18} />
            </button>
          </div>

          {drawer === 'sensitivity' ? (
            <div className="sensitivity-content">
              <p>
                Slider menguji logika klasifikasi demo. Nilai observasi garis dasar tidak berubah dan
                hasilnya bukan prediksi kebijakan.
              </p>
              <label>
                <span>Ambang integrasi <strong>{thresholds.integration.toFixed(2)}</strong></span>
                <input type="range" min="0.4" max="0.8" step="0.01" value={thresholds.integration} onChange={(event) => updateThreshold('integration', Number(event.target.value))} />
              </label>
              <label>
                <span>Ambang residual <strong>±{thresholds.residual.toFixed(2)}</strong></span>
                <input type="range" min="0.05" max="0.3" step="0.01" value={thresholds.residual} onChange={(event) => updateThreshold('residual', Number(event.target.value))} />
              </label>
              <label>
                <span>Kepekaan beban <strong>{thresholds.burden.toFixed(2)}</strong></span>
                <input type="range" min="0.35" max="0.8" step="0.01" value={thresholds.burden} onChange={(event) => updateThreshold('burden', Number(event.target.value))} />
              </label>
              <label>
                <span>Ambang ketahanan <strong>{thresholds.robustness.toFixed(2)}</strong></span>
                <input type="range" min="0.45" max="0.85" step="0.01" value={thresholds.robustness} onChange={(event) => updateThreshold('robustness', Number(event.target.value))} />
              </label>
              <button type="button" className="text-action" onClick={() => setThresholds(defaultThresholds)}>
                Pulihkan parameter demo
              </button>
            </div>
          ) : (
            <div className="evidence-content">
              <div className="scenario-note">
                <Layers3 size={18} />
                <div>
                  <strong>{selectedScenario.description}</strong>
                  <span>{selectedScenario.allowedClaim}</span>
                </div>
              </div>
              <div className="evidence-grid">
                {evidenceModules.map((module) => {
                  const status = selectedScenario.evidence[module.code];
                  return (
                    <article key={module.code}>
                      <div className="evidence-grid__title">
                        <code>{module.code}</code>
                        <span>{module.label}</span>
                        <i data-status={status}>{status === 'excluded' ? '∅' : status}</i>
                      </div>
                      <p>{module.note}</p>
                      <small>{module.year} · {module.unit} · {STATUS_LABELS[status]}</small>
                    </article>
                  );
                })}
              </div>
              <div className="gate-list">
                <div className="gate-list__title">
                  <ShieldCheck size={17} />
                  Empat gerbang label ketat
                </div>
                {gates.map((gate, index) => {
                  const activeCount = scenarioId === 'EV-FULL' ? 4 : scenarioId === 'EV-MIN' ? 2 : 1;
                  const active = index < activeCount;
                  return (
                    <div key={gate} className={active ? 'is-open' : ''}>
                      <span>{index + 1}</span>
                      <p>{gate}</p>
                      <strong>{active ? 'simulasi lolos' : 'belum lolos'}</strong>
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </section>
      )}

      <div className="fixed-boundary-note">
        <span /> Batas DKI tetap · jejak fungsional bukan yurisdiksi
      </div>
    </main>
  );
}
