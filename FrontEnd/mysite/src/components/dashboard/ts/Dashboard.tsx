import { useEffect, useState } from 'react';
import DashboardHeader from './DashboardHeader';
import '../css/Dashboard.css';

function Dashboard() {
  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
      window.location.href = '/login';
    }
  }, []);

  return (
    <div className="dashboard-wrapper">
      <DashboardHeader />
      <div className="dashboard-container">
        <div className="dashboard-content">
          <div className="dashboard-card">
            <h3>Profile</h3>
            <p>Welcome back!</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
