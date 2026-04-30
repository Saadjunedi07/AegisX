import { useEffect, useRef } from 'react';
import { incidentToMascotEvent, useAegisEmotion } from '../state/aegisEmotion';
import { useIncidents } from '../hooks/useIncidents';
import { FloatingAegisCard } from '../components/companion/FloatingAegisCard';

export function FloatingAssistant() {
  const { incidents, selectedIncident, selectIncident } = useIncidents();
  const mascot = useAegisEmotion('idle');
  const seenIncidentId = useRef<string | null>(null);

  useEffect(() => {
    const latest = incidents[0];
    if (!latest || latest.id === seenIncidentId.current) return;
    seenIncidentId.current = latest.id;
    mascot.dispatch(incidentToMascotEvent(latest), true);
  }, [incidents, mascot]);

  return (
    <div
      style={{
        minHeight: '100vh',
        display: 'grid',
        placeItems: 'center',
        background:
          'radial-gradient(circle at top, rgba(135,255,166,0.18), transparent 32%), linear-gradient(180deg, #070907, #0d120e 55%, #111712)',
        padding: '1.25rem',
      }}
    >
      <FloatingAegisCard
        incidents={incidents}
        selectedIncident={selectedIncident}
        mascotState={mascot.state}
        onSelectIncident={selectIncident}
        onActionStart={() => mascot.dispatch('action_running', true)}
        onActionComplete={(success) => mascot.dispatch(success ? 'action_success' : 'action_failed', true)}
        defaultExpanded
      />
    </div>
  );
}
