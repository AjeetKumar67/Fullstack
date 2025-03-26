import { useState } from 'react';
import Header from './components/Header';
import DashboardHeader from './components/DashboardHeader';
import Register from './components/Register';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Profile from './components/Profile';
import EditProfile from './components/EditProfile';
import './App.css';

function App() {
  const [view, setView] = useState<'register' | 'login' | 'dashboard' | 'profile' | 'editProfile'>('register');

  const handleLogin = () => {
    setView('dashboard');
  };

  const navigateToRegister = () => {
    setView('register');
  };

  const navigateToLogin = () => {
    setView('login');
  };

  const navigateToProfile = () => {
    setView('profile');
  };

  const navigateToEditProfile = () => {
    setView('editProfile');
  };

  const handleProfileUpdated = () => {
    setView('profile');
  };

  return (
    <div className="app-container">
      {view === 'dashboard' || view === 'profile' || view === 'editProfile' ? (
        <DashboardHeader onProfileClick={navigateToProfile} />
      ) : (
        <Header />
      )}
      <div className="content">
        {view === 'register' && <Register onNavigateToLogin={navigateToLogin} />}
        {view === 'login' && <Login onNavigateToRegister={navigateToRegister} onLogin={handleLogin} />}
        {view === 'dashboard' && <Dashboard />}
        {view === 'profile' && <Profile onEditProfile={navigateToEditProfile} />}
        {view === 'editProfile' && <EditProfile onProfileUpdated={handleProfileUpdated} />}
      </div>
    </div>
  );
}

export default App;
