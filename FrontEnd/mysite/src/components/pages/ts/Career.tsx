import '../css/Career.css';

function Career() {
  return (
    <div className="career-container">
      <div className="career-content">
        <h2>Career Opportunities</h2>
        
        <div className="job-listings">
          <div className="job-card">
            <h3>Senior Software Engineer</h3>
            <p className="job-location">Location: Remote</p>
            <p className="job-type">Type: Full-time</p>
            <div className="job-description">
              <h4>Requirements:</h4>
              <ul>
                <li>5+ years of experience in full-stack development</li>
                <li>Proficiency in React, TypeScript, and Node.js</li>
                <li>Experience with cloud platforms (AWS/Azure)</li>
              </ul>
            </div>
            <button className="apply-button">Apply Now</button>
          </div>

          <div className="job-card">
            <h3>UI/UX Designer</h3>
            <p className="job-location">Location: Hybrid</p>
            <p className="job-type">Type: Full-time</p>
            <div className="job-description">
              <h4>Requirements:</h4>
              <ul>
                <li>3+ years of UI/UX design experience</li>
                <li>Proficiency in Figma and Adobe Creative Suite</li>
                <li>Strong portfolio showcasing web/mobile designs</li>
              </ul>
            </div>
            <button className="apply-button">Apply Now</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Career;
