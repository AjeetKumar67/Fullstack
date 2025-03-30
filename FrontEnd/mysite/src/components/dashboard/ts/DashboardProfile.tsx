import { useState, useEffect } from 'react';
import '../css/DashboardProfile.css';

interface UserProfile {
  first_name: string;
  last_name: string;
  email: string;
  role: number;
  profile_picture: string;
}

function DashboardProfile() {
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState<UserProfile | null>(null);

  useEffect(() => {
    fetchProfile();
  }, []);

  const fetchProfile = async () => {
    try {
      const token = localStorage.getItem('accessToken');
      const response = await fetch('http://127.0.0.1:8000/api/profile/', {
        headers: {
          'Authorization': `Bearer ${token}`,
        }
      });

      if (!response.ok) throw new Error('Failed to fetch profile');
      
      const data = await response.json();
      setProfile(data);
      setFormData(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!formData) return;
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('accessToken');
      const response = await fetch('http://127.0.0.1:8000/api/profile/', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) throw new Error('Failed to update profile');
      
      const updatedData = await response.json();
      setProfile(updatedData);
      setIsEditing(false);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    }
  };

  if (loading) return <div className="dashboard-profile">Loading...</div>;
  if (error) return <div className="dashboard-profile error">{error}</div>;
  if (!profile) return <div className="dashboard-profile">No profile data found</div>;

  return (
    <div className="dashboard-profile">
      <div className="profile-header">
        <h2>Profile</h2>
        <button 
          className="edit-button"
          onClick={() => setIsEditing(!isEditing)}
        >
          {isEditing ? 'Cancel' : 'Edit Profile'}
        </button>
      </div>

      {isEditing ? (
        <form className="profile-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <label>First Name</label>
            <input
              type="text"
              name="first_name"
              value={formData?.first_name || ''}
              onChange={handleInputChange}
            />
          </div>
          <div className="form-group">
            <label>Last Name</label>
            <input
              type="text"
              name="last_name"
              value={formData?.last_name || ''}
              onChange={handleInputChange}
            />
          </div>
          <div className="form-group">
            <label>Email</label>
            <input
              type="email"
              name="email"
              value={formData?.email || ''}
              onChange={handleInputChange}
              disabled
            />
          </div>
          <div className="form-group">
            <label>Profile Picture URL</label>
            <input
              type="text"
              name="profile_picture"
              value={formData?.profile_picture || ''}
              onChange={handleInputChange}
            />
          </div>
          <button type="submit" className="save-button">Save Changes</button>
        </form>
      ) : (
        <div className="profile-info">
          <div className="profile-picture">
            <img src={profile.profile_picture || '/default-avatar.png'} alt="Profile" />
          </div>
          <div className="profile-details">
            <p><strong>Name:</strong> {profile.first_name} {profile.last_name}</p>
            <p><strong>Email:</strong> {profile.email}</p>
            <p><strong>Role:</strong> {profile.role === 1 ? 'Admin' : profile.role === 2 ? 'Staff' : 'User'}</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default DashboardProfile;
