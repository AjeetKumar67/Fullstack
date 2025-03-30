import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import Header from './components/header_footer/ts/Header';
import Home from './components/pages/ts/Home';
import About from './components/pages/ts/About';
import Career from './components/pages/ts/Career';
import Contact from './components/pages/ts/Contact';
import Login from './components/user/ts/Login';
import Register from './components/user/ts/Register';
import Dashboard from './components/dashboard/ts/Dashboard';
import './App.css';

function AppContent() {
  const location = useLocation();
  const isDashboard = location.pathname.startsWith('/dashboard');

  return (
    <div className="app-container">
      {!isDashboard && <Header />}
      <div className="content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/career" element={<Career />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/login" element={<Login onLogin={() => (window.location.href = '/dashboard')} />} />
          <Route path="/register" element={<Register onNavigateToLogin={() => (window.location.href = '/login')} />} />
          <Route path="/dashboard/*" element={<Dashboard />} />
        </Routes>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <AppContent />
    </Router>
  );
}

export default App;

