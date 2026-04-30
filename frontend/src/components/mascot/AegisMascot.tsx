import { AnimatePresence, motion } from 'framer-motion';
import type { MascotState } from '../../types';
import aegisAlert from '../../assets/aegis/aegis-alert.png';
import aegisCritical from '../../assets/aegis/aegis-critical.png';
import aegisHealing from '../../assets/aegis/aegis-healing.png';
import aegisIdle from '../../assets/aegis/aegis-idle.png';
import aegisMonitoring from '../../assets/aegis/aegis-monitoring.png';
import aegisScanning from '../../assets/aegis/aegis-scanning.png';
import aegisSleeping from '../../assets/aegis/aegis-sleeping.png';
import aegisSuccess from '../../assets/aegis/aegis-success.png';
import aegisThinking from '../../assets/aegis/aegis-thinking.png';
import { MASCOT_STATE_CONFIGS } from './MascotStates';
import styles from './mascot.module.css';

interface AegisMascotProps {
  state: MascotState;
  size?: number;
  showLabel?: boolean;
}

const AEGIS_STATE_ASSETS: Record<MascotState, string> = {
  idle: aegisIdle,
  monitoring: aegisMonitoring,
  scanning: aegisScanning,
  thinking: aegisThinking,
  alert: aegisAlert,
  critical: aegisCritical,
  healing: aegisHealing,
  success: aegisSuccess,
  sleeping: aegisSleeping,
};

const stateClassName = (state: MascotState) =>
  styles[`state${state.charAt(0).toUpperCase()}${state.slice(1)}` as keyof typeof styles] ?? '';

export function AegisMascot({ state, size = 120, showLabel = true }: AegisMascotProps) {
  const config = MASCOT_STATE_CONFIGS[state];

  return (
    <div
      className={styles.mascotContainer}
      style={{ width: size, ['--aegis-size' as string]: `${size}px`, ['--aegis-accent' as string]: config.accent }}
      aria-label={`Aegis mascot: ${config.label}`}
    >
      <motion.div
        key={state}
        className={`${styles.avatarStage} ${stateClassName(state)}`}
        initial={{ opacity: 0.9, scale: 0.97 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.18 }}
      >
        <img className={styles.avatarImage} src={AEGIS_STATE_ASSETS[state]} alt="" draggable={false} />
      </motion.div>

      <AnimatePresence mode="wait">
        {showLabel && (
          <motion.div
            key={state}
            className={styles.stateLabel}
            initial={{ opacity: 0, y: 5 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -5 }}
          >
            {config.label}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
