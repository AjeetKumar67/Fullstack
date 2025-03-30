import '../css/About.css';

function About() {
  return (
    <div className="about-container">
      <div className="about-content">
        <h2>About Us</h2>
        <div className="about-section">
          <h3>Our Mission</h3>
          <p>To provide innovative solutions that empower businesses and individuals to achieve their goals.</p>
        </div>
        
        <div className="about-section">
          <h3>Our Vision</h3>
          <p>To be a leading force in digital transformation and technological advancement.</p>
        </div>
        
        <div className="about-section">
          <h3>Our Values</h3>
          <ul>
            <li>Innovation and Creativity</li>
            <li>Customer Success</li>
            <li>Integrity and Trust</li>
            <li>Continuous Learning</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default About;
