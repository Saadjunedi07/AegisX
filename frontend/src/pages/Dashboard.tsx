import { useEffect, useRef } from 'react';
import { motion } from 'framer-motion';
import logo from '../assets/logo.png';
import { FloatingAegisCard } from '../components/companion/FloatingAegisCard';
import { useActions } from '../hooks/useActions';
import { useIncidents } from '../hooks/useIncidents';
import { useMetrics } from '../hooks/useMetrics';
import { incidentToMascotEvent, metricsToMascotEvent, useAegisEmotion } from '../state/aegisEmotion';
import type { ActionType, Incident } from '../types';
import { ACTION_LABELS, INCIDENT_TYPE_ICONS, INCIDENT_TYPE_LABELS, SEVERITY_COLORS } from '../utils/constants';
import { formatBytes, formatTimestampFull, timeAgo } from '../utils/formatters';
import styles from './dashboard.module.css';

const NAV_ITEMS = [
  ['Dashboard', 'DA'],
  ['Incidents', 'IN'],
  ['Monitoring', 'MO'],
  ['Network', 'NW'],
  ['Logs', 'LG'],
  ['Automation', 'AU'],
  ['Settings', 'ST'],
] as const;

const QUICK_ACTIONS: ActionType[] = ['run_scan', 'block_ip', 'restart_service', 'view_logs'];

export function Dashboard() {
  const { incidents, selectedIncident, analysis, analysisLoading, selectIncident, isConnected } = useIncidents();
  const { metrics, loading: metricsLoading } = useMetrics();
  const { execute, executing, lastResult } = useActions();
  const mascot = useAegisEmotion('idle');
  const seenIncidentId = useRef<string | null>(null);

  useEffect(() => {
    const latest = incidents[0];
    if (!latest || latest.id === seenIncidentId.current) return;
    seenIncidentId.current = latest.id;
    mascot.dispatch(incidentToMascotEvent(latest), true);
  }, [incidents, mascot]);

  useEffect(() => {
    if (analysisLoading) mascot.dispatch('analysis_started', true);
  }, [analysisLoading, mascot]);

  useEffect(() => {
    if (!metricsLoading) mascot.dispatch(metricsToMascotEvent(metrics));
  }, [metrics, metricsLoading, mascot]);

  const latestIncident = selectedIncident ?? incidents[0] ?? null;
  const unresolvedIncidents = incidents.filter((incident) => !incident.is_resolved);
  const activeIncidents = unresolvedIncidents.length;
  const criticalIncidents = unresolvedIncidents.filter((incident) => incident.severity === 'critical').length;
  const threatLevel = latestIncident?.severity ?? 'low';
  const healthScore = calculateHealthScore(metrics);
  const activitySeries = createActivitySeries(metrics);
  const heatmapCells = createHeatmapCells(incidents);

  const handleQuickAction = async (actionType: ActionType) => {
    if (!latestIncident) return;

    const target =
      actionType === 'block_ip'
        ? latestIncident.source_ip
        : latestIncident.affected_service;

    mascot.dispatch('action_running', true);
    const result = await execute(actionType, target, latestIncident.id);
    mascot.dispatch(result?.status === 'success' ? 'action_success' : 'action_failed', true);
  };

  return (
    <div className={styles.page}>
      <div className={styles.shell}>
        <aside className={styles.sidebar}>
          <div className={styles.logoDock}>
            <div className={styles.logoBadge}>
              <img src={logo} alt="AegisX logo" />
            </div>
          </div>

          <nav className={styles.nav} aria-label="Primary">
            {NAV_ITEMS.map(([label, glyph], index) => (
              <button
                key={label}
                type="button"
                className={`${styles.navItem} ${index === 0 ? styles.navActive : ''}`}
              >
                <span className={styles.navGlyph}>{glyph}</span>
                <span className={styles.navLabel}>{label}</span>
              </button>
            ))}
          </nav>
        </aside>

        <main className={styles.main}>
          <div className={styles.topBar}>
            <section className={styles.brandBar}>
              <div className={styles.brandLogo}>
                <img src={logo} alt="AegisX shield logo" />
              </div>
              <div className={styles.brandCopy}>
                <span className={styles.overline}>Autonomous AI Defense</span>
                <h1 className={styles.brandName}>AegisX Control Deck</h1>
                <p className={styles.brandCaption}>Editorial-grade observability with retro pixel-tech signal design.</p>
              </div>
            </section>

            <section className={styles.utilityBar}>
              <label className={styles.search}>
                <span>SR</span>
                <input type="text" value="Search incidents, hosts, playbooks" readOnly />
              </label>
              <div className={styles.healthBadge}>
                <span className={styles.healthDot} />
                {isConnected ? 'System healthy' : 'Feed reconnecting'}
              </div>
              <button type="button" className={styles.iconButton}>NB</button>
              <button type="button" className={styles.profileButton}>
                <span>AD</span>
                <span>OPS</span>
              </button>
            </section>
          </div>

          <section className={styles.hero}>
            <div className={styles.heroGrid}>
              <div>
                <motion.h2
                  className={styles.heroTitle}
                  initial={{ opacity: 0, y: 14 }}
                  animate={{ opacity: 1, y: 0 }}
                >
                  AegisX <span>Security Overview</span>
                </motion.h2>
                <p className={styles.heroCopy}>
                  Autonomous AI Incident Analyst and Auto-Response Agent for threat visibility, service resilience,
                  network observability, and response orchestration.
                </p>
                <div className={styles.heroMeta}>
                  <span className={styles.metaPill}>Threat posture {threatLevel}</span>
                  <span className={styles.metaPill}>{activeIncidents} active incidents</span>
                  <span className={styles.metaPill}>health score {healthScore}</span>
                  <span className={styles.metaPill}>mascot state {mascot.state}</span>
                </div>
              </div>

              <div className={styles.heroAside}>
                <div className={styles.signalCard}>
                  <div className={styles.signalLabel}>Threat Level</div>
                  <div className={styles.signalValue}>{threatLevel.toUpperCase()}</div>
                  <div className={styles.signalText}>
                    {latestIncident ? latestIncident.description : 'No active threat surge. Aegis is monitoring quietly.'}
                  </div>
                </div>
                <div className={styles.signalCard}>
                  <div className={styles.signalLabel}>Network Throughput</div>
                  <div className={styles.signalValue}>{metrics ? formatBytes(metrics.network_bytes_recv) : '0 B'}</div>
                  <div className={styles.signalText}>
                    Current inbound stream with {metrics?.network_connections ?? 0} active connections.
                  </div>
                </div>
              </div>
            </div>
          </section>

          <section className={styles.bodyGrid}>
            <div className={styles.column}>
              <div className={styles.grid2}>
                <StatCard
                  eyebrow="Threat Level"
                  title="Priority posture"
                  value={threatLevel.toUpperCase()}
                  detail={`${criticalIncidents} critical incidents in the queue`}
                />
                <StatCard
                  eyebrow="Active Incidents"
                  title="Live operational load"
                  value={String(activeIncidents).padStart(2, '0')}
                  detail={`${incidents.length} incidents received in session`}
                />
              </div>

              <div className={styles.card}>
                <div className={styles.cardHeader}>
                  <div>
                    <div className={styles.cardEyebrow}>Incident Feed</div>
                    <div className={styles.cardTitle}>Live detections</div>
                  </div>
                  <div className={styles.cardValueSmall}>{incidents.length} tracked</div>
                </div>
                <div className={styles.incidentStack}>
                  {incidents.slice(0, 5).map((incident) => (
                    <button
                      key={incident.id}
                      type="button"
                      className={`${styles.incidentCard} ${selectedIncident?.id === incident.id ? styles.incidentSelected : ''}`}
                      onClick={() => selectIncident(incident)}
                    >
                      <div className={styles.incidentHeadline}>
                        <span>{INCIDENT_TYPE_ICONS[incident.type]} {INCIDENT_TYPE_LABELS[incident.type]}</span>
                        <span
                          className={styles.severityPill}
                          style={{ color: SEVERITY_COLORS[incident.severity] }}
                        >
                          {incident.severity}
                        </span>
                      </div>
                      <div className={styles.incidentDesc}>{incident.affected_service} {String.fromCharCode(8226)} {timeAgo(incident.timestamp)}</div>
                    </button>
                  ))}
                </div>
              </div>

              <div className={styles.card}>
                <div className={styles.cardHeader}>
                  <div>
                    <div className={styles.cardEyebrow}>Quick Actions</div>
                    <div className={styles.cardTitle}>Auto-response deck</div>
                  </div>
                  <div className={styles.cardValueSmall}>{executing ? 'Running' : 'Standby'}</div>
                </div>
                <div className={styles.actionGrid}>
                  {QUICK_ACTIONS.map((actionType) => (
                    <button
                      key={actionType}
                      type="button"
                      className={styles.actionButton}
                      disabled={executing || !latestIncident}
                      onClick={() => handleQuickAction(actionType)}
                    >
                      <span className={styles.actionKicker}>{actionType.replace('_', ' ')}</span>
                      <span className={styles.actionCopy}>{ACTION_LABELS[actionType]}</span>
                    </button>
                  ))}
                </div>
                {lastResult && (
                  <p className={styles.analysisCopy} style={{ marginTop: '0.85rem' }}>
                    {lastResult.message} {String.fromCharCode(8226)} {lastResult.duration_ms}ms
                  </p>
                )}
              </div>
            </div>

            <div className={styles.column}>
              <div className={styles.card}>
                <div className={styles.cardHeader}>
                  <div>
                    <div className={styles.cardEyebrow}>AI Analysis</div>
                    <div className={styles.cardTitle}>Autonomous incident brief</div>
                  </div>
                  <div className={`${styles.cardValue} ${styles.cardValueSmall}`}>
                    {analysisLoading ? 'Thinking' : analysis ? `${Math.round(analysis.confidence * 100)}%` : '--'}
                  </div>
                </div>
                {analysis ? (
                  <div className={styles.analysisGrid}>
                    <div>
                      <div className={styles.cardEyebrow}>What happened</div>
                      <p className={styles.analysisCopy}>{analysis.what_happened}</p>
                    </div>
                    <div className={styles.analysisBlock}>
                      <div className={styles.cardEyebrow}>Why it happened</div>
                      <p className={styles.analysisCopy}>{analysis.why_it_happened}</p>
                    </div>
                    <div className={styles.analysisBlock}>
                      <div className={styles.cardEyebrow}>Suggested action</div>
                      <p className={styles.analysisCopy}>{analysis.suggested_action}</p>
                    </div>
                  </div>
                ) : (
                  <p className={styles.mutedCopy}>
                    Select an incident to open the AI analysis brief. Aegis will move into the thinking state while the report is generated.
                  </p>
                )}
              </div>

              <div className={styles.card}>
                <div className={styles.cardHeader}>
                  <div>
                    <div className={styles.cardEyebrow}>Threat Heatmap</div>
                    <div className={styles.cardTitle}>Alert density and log pulse</div>
                  </div>
                  <div className={styles.cardValueSmall}>Last 24 frames</div>
                </div>
                <div className={styles.chartBox}>
                  <div className={styles.heatmap}>
                    {heatmapCells.map((cell, index) => (
                      <div
                        key={`${cell.label}-${index}`}
                        className={styles.heatCell}
                        style={{ background: cell.color }}
                        title={cell.label}
                      />
                    ))}
                  </div>
                  <div className={styles.logList}>
                    {incidents.slice(0, 4).map((incident) => (
                      <div key={incident.id} className={styles.logRow}>
                        <span>{timeAgo(incident.timestamp)}</span>
                        <span>{incident.description}</span>
                        <span style={{ color: SEVERITY_COLORS[incident.severity] }}>{incident.severity}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>

            <div className={styles.column}>
              <div className={styles.card}>
                <div className={styles.cardHeader}>
                  <div>
                    <div className={styles.cardEyebrow}>System Health</div>
                    <div className={styles.cardTitle}>Core service stability</div>
                  </div>
                  <div className={styles.cardValue}>{healthScore}</div>
                </div>
                <div className={styles.statList}>
                  <ProgressRow label="CPU" value={metrics?.cpu_percent ?? 0} />
                  <ProgressRow label="Memory" value={metrics?.memory_percent ?? 0} />
                  <ProgressRow label="Disk" value={metrics?.disk_percent ?? 0} />
                </div>
              </div>

              <div className={styles.card}>
                <div className={styles.cardHeader}>
                  <div>
                    <div className={styles.cardEyebrow}>Threat Logs Chart</div>
                    <div className={styles.cardTitle}>Signal waveform</div>
                  </div>
                  <div className={styles.cardValueSmall}>{latestIncident ? formatTimestampFull(latestIncident.timestamp) : 'Live'}</div>
                </div>
                <div className={styles.chartBox}>
                  <svg className={styles.lineChart} viewBox="0 0 400 180" preserveAspectRatio="none">
                    <defs>
                      <linearGradient id="activity-gradient" x1="0" x2="1">
                        <stop offset="0%" stopColor="#7effa7" />
                        <stop offset="100%" stopColor="#62d8ff" />
                      </linearGradient>
                    </defs>
                    <path
                      d={buildLinePath(activitySeries)}
                      fill="none"
                      stroke="url(#activity-gradient)"
                      strokeWidth="4"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    />
                  </svg>
                </div>
              </div>

              <div className={styles.card}>
                <div className={styles.cardHeader}>
                  <div>
                    <div className={styles.cardEyebrow}>Network Activity</div>
                    <div className={styles.cardTitle}>Inbound and outbound flows</div>
                  </div>
                  <div className={styles.cardValueSmall}>{metrics?.network_connections ?? 0} conns</div>
                </div>
                <div className={styles.networkBars}>
                  <NetworkRow label="Inbound" value={metrics ? normalizeTraffic(metrics.network_bytes_recv) : 0} text={metrics ? formatBytes(metrics.network_bytes_recv) : '0 B'} />
                  <NetworkRow label="Outbound" value={metrics ? normalizeTraffic(metrics.network_bytes_sent) : 0} text={metrics ? formatBytes(metrics.network_bytes_sent) : '0 B'} />
                  <NetworkRow label="Sockets" value={Math.min(((metrics?.network_connections ?? 0) / 1000) * 100, 100)} text={String(metrics?.network_connections ?? 0)} />
                </div>
              </div>
            </div>
          </section>
        </main>
      </div>

      <div className={styles.floatingDock}>
        <FloatingAegisCard
          incidents={incidents}
          selectedIncident={selectedIncident}
          mascotState={mascot.state}
          onSelectIncident={selectIncident}
          onActionStart={(actionType) => {
            mascot.dispatch('action_running', true);
            if (actionType === 'run_scan') mascot.dispatch('scan_started', true);
          }}
          onActionComplete={(success) => mascot.dispatch(success ? 'action_success' : 'action_failed', true)}
        />
      </div>
    </div>
  );
}

function StatCard({ eyebrow, title, value, detail }: { eyebrow: string; title: string; value: string; detail: string }) {
  return (
    <div className={styles.card}>
      <div className={styles.cardHeader}>
        <div>
          <div className={styles.cardEyebrow}>{eyebrow}</div>
          <div className={styles.cardTitle}>{title}</div>
        </div>
        <div className={styles.cardValue}>{value}</div>
      </div>
      <p className={styles.mutedCopy}>{detail}</p>
    </div>
  );
}

function ProgressRow({ label, value }: { label: string; value: number }) {
  return (
    <div className={styles.statRow}>
      <span className={styles.statLabel}>{label}</span>
      <div className={styles.progressTrack}>
        <div className={styles.progressFill} style={{ width: `${Math.min(Math.max(value, 2), 100)}%` }} />
      </div>
      <span className={styles.cardValueSmall}>{Math.round(value)}%</span>
    </div>
  );
}

function NetworkRow({ label, value, text }: { label: string; value: number; text: string }) {
  return (
    <div className={styles.networkRow}>
      <span>{label}</span>
      <div className={styles.barTrack}>
        <div className={styles.barFill} style={{ width: `${Math.min(Math.max(value, 3), 100)}%` }} />
      </div>
      <span>{text}</span>
    </div>
  );
}

function calculateHealthScore(metrics: ReturnType<typeof useMetrics>['metrics']) {
  if (!metrics) return '88';
  const meanLoad = (metrics.cpu_percent + metrics.memory_percent + metrics.disk_percent) / 3;
  return String(Math.max(42, Math.round(100 - meanLoad)));
}

function normalizeTraffic(bytes: number) {
  if (bytes <= 0) return 0;
  return Math.min(100, Math.round((Math.log10(bytes + 1) / 9) * 100));
}

function createActivitySeries(metrics: ReturnType<typeof useMetrics>['metrics']) {
  const cpu = metrics?.cpu_percent ?? 34;
  const mem = metrics?.memory_percent ?? 42;
  const disk = metrics?.disk_percent ?? 26;
  return [cpu * 0.55, mem * 0.8, cpu, disk * 0.9, mem * 0.72, cpu * 0.64, disk * 1.08, mem * 0.66];
}

function buildLinePath(values: number[]) {
  const stepX = 400 / Math.max(values.length - 1, 1);
  return values
    .map((value, index) => `${index === 0 ? 'M' : 'L'} ${index * stepX} ${170 - value * 1.2}`)
    .join(' ');
}

function createHeatmapCells(incidents: Incident[]) {
  const fallback = Array.from({ length: 24 }, (_, index) => ({
    label: `Quiet window ${index + 1}`,
    color: index % 5 === 0 ? 'rgba(113, 255, 145, 0.55)' : 'rgba(57, 84, 62, 0.7)',
  }));

  if (!incidents.length) return fallback;

  return Array.from({ length: 24 }, (_, index) => {
    const incident = incidents[index % incidents.length];
    const severityColor = SEVERITY_COLORS[incident.severity];
    return {
      label: `${INCIDENT_TYPE_LABELS[incident.type]} ${String.fromCharCode(8226)} ${incident.severity}`,
      color: `${severityColor}${incident.severity === 'critical' ? 'ee' : incident.severity === 'high' ? 'cc' : '99'}`,
    };
  });
}
