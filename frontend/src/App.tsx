/* ── AegisX App Root ── */

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import DashboardModern from './pages/DashboardModern';
import { FloatingAssistant } from './pages/FloatingAssistant';

function App() {
  return (
    <BrowserRouter basename={import.meta.env.BASE_URL}>
      <Routes>
        <Route path="/" element={<DashboardModern />} />
        <Route path="/floating" element={<FloatingAssistant />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
