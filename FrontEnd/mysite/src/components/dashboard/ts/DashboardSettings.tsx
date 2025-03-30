import '../css/DashboardSettings.css';

function DashboardSettings() {
  return (
    <div className="dashboard-settings">
      <h2>Settings</h2>
      <div className="settings-grid">
        <div className="settings-card">
          <h3>Account Settings</h3>
          <div className="settings-form">
            <div className="form-group">
              <label>Email Notifications</label>
              <input type="checkbox" />
            </div>
            <div className="form-group">
              <label>Dark Mode</label>
              <input type="checkbox" />
            </div>
            <div className="form-group">
              <label>Language</label>
              <select>
                <option value="en">English</option>
                <option value="es">Spanish</option>
              </select>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default DashboardSettings;
