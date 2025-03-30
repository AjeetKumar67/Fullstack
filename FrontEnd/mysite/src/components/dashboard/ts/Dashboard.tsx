import { Routes, Route } from 'react-router-dom';
import DashboardHeader from './DashboardHeader';
import DashboardHome from './DashboardHome';
import DashboardSettings from './DashboardSettings';
import DashboardProfile from './DashboardProfile';
import '../css/Dashboard.css';

function Dashboard() {
  return (
    <div className="dashboard-wrapper">
      <DashboardHeader />
      <div className="dashboard-container">
        <Routes>
          <Route path="/" element={<DashboardHome />} />
          <Route path="/settings" element={<DashboardSettings />} />
          <Route path="/profile" element={<DashboardProfile />} />
        </Routes>
      </div>
    </div>
  );
}

export default Dashboard;
