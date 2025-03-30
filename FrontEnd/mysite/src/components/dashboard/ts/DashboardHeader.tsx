import '../css/DashboardHeader.css';

function DashboardHeader() {
  const handleLogout = () => {
    localStorage.removeItem('accessToken');
    window.location.href = '/login';
  };

  return (
    <header className="dashboard-header-container">
      <h1>Dashboard</h1>
      <nav>
        <a href="/dashboard">Home</a>
        <a href="/dashboard/profile">Profile</a>
        <a href="/dashboard/settings">Settings</a>
        <button className="logout-link" onClick={handleLogout}>Logout</button>
      </nav>
    </header>
  );
}

export default DashboardHeader;
