import { NavLink } from 'react-router-dom';
import { siteLogo } from '../../../utils/backgroundImages';
import '../css/Header.css';

function Header() {
  return (
    <header className="header-container">
      <div className="logo-container">
        <img src={siteLogo} alt="Ajeet Logo" className="site-logo" />
      </div>
      <nav>
        <NavLink to="/" className={({ isActive }) => isActive ? 'active' : ''}>
          Home
        </NavLink>
        <NavLink to="/about" className={({ isActive }) => isActive ? 'active' : ''}>
          About
        </NavLink>
        <NavLink to="/career" className={({ isActive }) => isActive ? 'active' : ''}>
          Career
        </NavLink>
        <NavLink to="/contact" className={({ isActive }) => isActive ? 'active' : ''}>
          Contact
        </NavLink>
        <NavLink to="/register" className={({ isActive }) => isActive ? 'active' : ''}>
          Register
        </NavLink>
      </nav>
    </header>
  );
}

export default Header;
