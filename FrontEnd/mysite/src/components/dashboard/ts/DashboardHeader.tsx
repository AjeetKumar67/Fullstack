import { Link, useNavigate } from 'react-router-dom';
import '../css/DashboardHeader.css';

function DashboardHeader() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('accessToken');
    navigate('/login');
  };

  return (
    <header className="dashboard-header-container">
      <h1>Dashboard</h1>
      <nav>
        <Link to="/dashboard">Home</Link>
        <Link to="/dashboard/profile">Profile</Link>
        <Link to="/dashboard/settings">Settings</Link>
        <button className="logout-link" onClick={handleLogout}>Logout</button>
      </nav>
    </header>
  );
}

export default DashboardHeader;
