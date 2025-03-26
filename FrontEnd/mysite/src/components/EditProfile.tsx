import { useEffect, useState } from 'react';
import './EditProfile.css';

function EditProfile({ onProfileUpdated }: { onProfileUpdated: () => void }) {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    profilePicture: '',
  });
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUserProfile = async () => {
      try {
        const token = localStorage.getItem('accessToken');
        if (!token) {
          setMessage('No access token found. Please log in.');
          return;
        }

        const response = await fetch('http://127.0.0.1:8000/api/profile/', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
          },
        });

        if (response.ok) {
          const data = await response.json();
          setFormData({
            firstName: data.first_name,
            lastName: data.last_name,
            email: data.email, // Email is prefilled and non-editable
            profilePicture: data.profile_picture || '',
          });
        } else {
          setMessage('Failed to fetch user profile.');
        }
      } catch (error) {
        setMessage('An error occurred while fetching the profile.');
      } finally {
        setLoading(false);
      }
    };

    fetchUserProfile();
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('accessToken');
      const response = await fetch('http://127.0.0.1:8000/api/profile/', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setMessage('Profile updated successfully!');
        onProfileUpdated(); // Navigate back to the profile page
      } else {
        const errorData = await response.json();
        setMessage(errorData.error || 'Failed to update profile.');
      }
    } catch (error) {
      setMessage('An error occurred. Please try again.');
    }
  };

  if (loading) {
    return <div className="edit-profile-container"><p>Loading...</p></div>;
  }

  return (
    <div className="edit-profile-container">
      <h2>Edit Profile</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="firstName"
          placeholder="First Name"
          value={formData.firstName}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="lastName"
          placeholder="Last Name"
          value={formData.lastName}
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          readOnly // Make email non-editable
        />
        <input
          type="text"
          name="profilePicture"
          placeholder="Profile Picture URL"
          value={formData.profilePicture}
          onChange={handleChange}
        />
        <button type="submit">Save Changes</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default EditProfile;
