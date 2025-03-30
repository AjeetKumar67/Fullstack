import { NavLink } from 'react-router-dom';
import '../css/Header.css';

function Header() {
  return (
    <header className="header-container">
      <h1>MySite</h1>
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
