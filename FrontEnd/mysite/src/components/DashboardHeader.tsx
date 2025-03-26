import './DashboardHeader.css';

function DashboardHeader({ onProfileClick }: { onProfileClick: () => void }) {
  return (
    <header className="dashboard-header-container">
      <h1>Dashboard</h1>
      <nav>
        <a href="#overview">Overview</a>
        <button className="profile-link" onClick={onProfileClick}>
          Profile
        </button>
        <a href="#settings">Settings</a>
        <a href="#logout">Logout</a>
      </nav>
    </header>
  );
}

export default DashboardHeader;
