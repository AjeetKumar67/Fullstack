import './Header.css';

function Header() {
  return (
    <header className="header-container">
      <h1>MySite</h1>
      <nav>
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
        <a href="#logout">Logout</a>
        <a href="#Career">Career</a>
      </nav>
    </header>
  );
}

export default Header;
