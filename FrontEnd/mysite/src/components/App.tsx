import { useState } from 'react';
import Header from './components/Header';
import Register from './components/Register';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import './App.css';

function App() {
  const [view, setView] = useState<'register' | 'login' | 'dashboard'>('register');

  const handleLogin = () => {
    setView('dashboard');
  };

  const navigateToRegister = () => {
    setView('register');
  };

  const navigateToLogin = () => {
    setView('login');
  };

  return (
    <div className="app-container">
      <Header />
      <div className="content">
        {view === 'register' && <Register onNavigateToLogin={navigateToLogin} />}
        {view === 'login' && <Login onNavigateToRegister={navigateToRegister} onLogin={handleLogin} />}
        {view === 'dashboard' && <Dashboard />}
      </div>
    </div>
  );
}

export default App;
