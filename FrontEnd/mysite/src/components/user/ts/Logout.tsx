import { useEffect } from 'react';
import '../css/Logout.css';

function Logout({ onLogoutSuccess }: { onLogoutSuccess: () => void }) {
  useEffect(() => {
    const performLogout = async () => {
      try {
        const token = localStorage.getItem('accessToken');
        if (!token) {
          onLogoutSuccess();
          return;
        }

        const response = await fetch('http://127.0.0.1:8000/api/logout/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify({ refresh: token }),
        });

        if (response.ok) {
          localStorage.removeItem('accessToken');
        }
      } catch (error) {
        console.error('Logout error:', error);
      } finally {
        onLogoutSuccess();
      }
    };

    performLogout();
  }, [onLogoutSuccess]);

  return (
    <div className="logout-container">
      <p>Logging out...</p>
    </div>
  );
}

export default Logout;
