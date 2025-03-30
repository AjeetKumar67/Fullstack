import '../css/DashboardHome.css';

function DashboardHome() {
  return (
    <div className="dashboard-home">
      <h2>Welcome to Dashboard</h2>
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Total Users</h3>
          <p>1,234</p>
        </div>
        <div className="stat-card">
          <h3>Active Projects</h3>
          <p>25</p>
        </div>
        <div className="stat-card">
          <h3>Tasks Completed</h3>
          <p>789</p>
        </div>
      </div>
    </div>
  );
}

export default DashboardHome;
