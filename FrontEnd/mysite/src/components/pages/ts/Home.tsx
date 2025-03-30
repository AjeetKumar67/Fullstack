import { useEffect, useState } from 'react';
import '../css/Home.css';

function Home() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  return (
    <div className="home-container">
      <h1 className="page-title">Home Page</h1>
      <div className={`home-content ${isVisible ? 'visible' : ''}`}>
        <h1>Welcome to Our Website</h1>
        <p className="tagline">Building Tomorrow's Solutions Today</p>
        
        <div className="features-grid">
          <div className="feature-card">
            <h3>Innovation</h3>
            <p>Cutting-edge solutions for modern challenges</p>
          </div>
          <div className="feature-card">
            <h3>Excellence</h3>
            <p>Committed to delivering the highest quality</p>
          </div>
          <div className="feature-card">
            <h3>Partnership</h3>
            <p>Building lasting relationships with clients</p>
          </div>
          <div className="feature-card">
            <h3>Growth</h3>
            <p>Continuous improvement and development</p>
          </div>
        </div>

        <div className="cta-section">
          <button className="cta-button">Get Started</button>
          <button className="cta-button secondary">Learn More</button>
        </div>
      </div>
    </div>
  );
}

export default Home;
