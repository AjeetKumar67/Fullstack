import { useEffect, useState } from 'react';
import '../css/Profile.css';

interface UserProfile {
  name: string;
  email: string;
  role: string;
  profilepicture: string;
}

function Profile({ onEditProfile }: { onEditProfile: () => void }) {
  const [user, setUser] = useState<UserProfile | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchUserProfile = async () => {
      try {
        const token = localStorage.getItem('accessToken'); // Retrieve JWT token from localStorage
        if (!token) {
          setError('No access token found. Please log in.');
          return;
        }

        const response = await fetch('http://127.0.0.1:8000/api/profile/', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`, // Send JWT token in Authorization header
          },
        });

        if (response.ok) {
          const data = await response.json();
          setUser({
            name: `${data.first_name} ${data.last_name}`,
            email: data.email,
            profilepicture: data.profile_picture,
            role: data.role === 1 ? 'Admin' : data.role === 2 ? 'Staff' : 'User',
          });
        } else {
          setError('Failed to fetch user profile.');
        }
      } catch (err) {
        setError('An error occurred while fetching the profile.');
      }
    };

    fetchUserProfile();
  }, []);

  if (error) {
    return <div className="profile-container"><p className="error">{error}</p></div>;
  }

  if (!user) {
    return <div className="profile-container"><p>Loading...</p></div>;
  }

  return (
    <div className="profile-container">
      <h2>Profile Details</h2>
      <p><strong>Name:</strong> {user.name}</p>
      <p><strong>Email:</strong> {user.email}</p>
      <p><strong>Role:</strong> {user.role}</p>
      <p><strong>Profile Picture:</strong> {user.profilepicture}</p>
      <button className="edit-profile-button" onClick={onEditProfile}>
        Edit Profile
      </button>
    </div>
  );
}

export default Profile;
