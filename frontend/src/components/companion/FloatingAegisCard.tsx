import { useState } from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import { AegisMascot } from '../mascot/AegisMascot';
import { useActions } from '../../hooks/useActions';
import type { ActionType, Incident, MascotState } from '../../types';
import { ACTION_LABELS, INCIDENT_TYPE_ICONS, INCIDENT_TYPE_LABELS, SEVERITY_COLORS } from '../../utils/constants';
import { timeAgo } from '../../utils/formatters';
import styles from './companion.module.css';

interface FloatingAegisCardProps {
  incidents: Incident[];
  selectedIncident: Incident | null;
  mascotState: MascotState;
  onSelectIncident: (incident: Incident) => void;
  onActionStart?: (actionType: ActionType) => void;
  onActionComplete?: (success: boolean) => void;
  compact?: boolean;
  defaultExpanded?: boolean;
}

const ACTIONS: ActionType[] = ['run_scan', 'block_ip', 'restart_service', 'view_logs'];

export function FloatingAegisCard({
  incidents,
  selectedIncident,
  mascotState,
  onSelectIncident,
  onActionStart,
  onActionComplete,
  compact = false,
  defaultExpanded = true,
}: FloatingAegisCardProps) {
  const [expanded, setExpanded] = useState(defaultExpanded && !compact);
  const { execute, executing, lastResult } = useActions();

  const criticalCount = incidents.filter((incident) => incident.severity === 'critical').length;
  const highCount = incidents.filter((incident) => incident.severity === 'high').length;
  const targetIncident = selectedIncident ?? incidents[0] ?? null;

  const handleAction = async (actionType: ActionType) => {
    if (!targetIncident) return;

    const target =
      actionType === 'block_ip'
        ? targetIncident.source_ip
        : actionType === 'restart_service'
          ? targetIncident.affected_service
          : actionType === 'view_logs'
            ? targetIncident.affected_service
            : targetIncident.affected_service;

    onActionStart?.(actionType);
    const result = await execute(actionType, target, targetIncident.id);
    onActionComplete?.(result?.status === 'success');
  };

  return (
    <motion.aside
      drag
      dragMomentum={false}
      whileDrag={{ scale: 1.015, rotate: -1 }}
      className={`${styles.floatingCard} ${compact ? styles.floatingCardCompact : ''} ${compact ? styles.compact : ''}`}
    >
      <div className={styles.companionHeader} onClick={() => !compact && setExpanded((value) => !value)}>
        <div className={styles.companionTitle}>
          <span className={styles.eyebrow}>Pixel Companion</span>
          <span className={styles.title}>Aegis Live</span>
        </div>
        <div className={styles.statusStack}>
          <span className={`${styles.chip} ${styles.chipState}`}>{mascotState}</span>
          {criticalCount > 0 && <span className={`${styles.chip} ${styles.chipCritical}`}>{criticalCount} crit</span>}
          {highCount > 0 && <span className={`${styles.chip} ${styles.chipHigh}`}>{highCount} high</span>}
        </div>
      </div>

      <div className={styles.companionBody}>
        <div className={styles.avatarWrap}>
          <AegisMascot state={mascotState} size={compact ? 104 : 156} showLabel={!compact} />
        </div>

        <AnimatePresence initial={false}>
          {(expanded || !compact) && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              transition={{ duration: 0.2 }}
              style={{ display: 'grid', gap: '0.9rem' }}
            >
              <div className={styles.incidentList}>
                {incidents.slice(0, 4).map((incident) => (
                  <button
                    key={incident.id}
                    type="button"
                    className={`${styles.incidentButton} ${selectedIncident?.id === incident.id ? styles.incidentActive : ''}`}
                    onClick={() => onSelectIncident(incident)}
                  >
                    <div className={styles.incidentTop}>
                      <span>
                        {INCIDENT_TYPE_ICONS[incident.type]} {INCIDENT_TYPE_LABELS[incident.type]}
                      </span>
                      <span
                        className={styles.pill}
                        style={{
                          color: SEVERITY_COLORS[incident.severity],
                          borderColor: SEVERITY_COLORS[incident.severity],
                        }}
                      >
                        {incident.severity}
                      </span>
                    </div>
                    <div className={styles.incidentMeta}>
                      {incident.affected_service} {String.fromCharCode(8226)} {timeAgo(incident.timestamp)}
                    </div>
                  </button>
                ))}
              </div>

              <div className={styles.actionRow}>
                {ACTIONS.map((actionType) => (
                  <button
                    key={actionType}
                    type="button"
                    className={styles.actionButton}
                    onClick={() => handleAction(actionType)}
                    disabled={executing || !targetIncident}
                  >
                    <span className={styles.actionGlyph}>{actionType === 'run_scan' ? 'S' : actionType === 'block_ip' ? 'B' : actionType === 'restart_service' ? 'R' : 'L'}</span>
                    <span>{ACTION_LABELS[actionType]}</span>
                  </button>
                ))}
              </div>

              {lastResult && (
                <div className={styles.result}>
                  {lastResult.message} {String.fromCharCode(8226)} {lastResult.duration_ms}ms
                </div>
              )}
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </motion.aside>
  );
}
