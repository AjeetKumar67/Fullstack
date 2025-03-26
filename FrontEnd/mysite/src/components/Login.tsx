import { useState } from 'react';
import './Login.css';

function Login({ onNavigateToRegister, onLogin }: { onNavigateToRegister: () => void; onLogin: () => void }) {
  const [formData, setFormData] = useState({ email: '', password: '' });
  const [message, setMessage] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:8000/api/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        const data = await response.json();
        localStorage.setItem('accessToken', data.access); // Store JWT token in localStorage
        setMessage('Login successful!');
        onLogin(); // Navigate to Dashboard
      } else {
        const errorData = await response.json();
        setMessage(errorData.error || 'Login failed.');
      }
    } catch (error) {
      setMessage('An error occurred. Please try again.');
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
        <input type="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} required />
        <button type="submit">Login</button>
      </form>
      {message && <p>{message}</p>}
      <button className="navigate-button" onClick={onNavigateToRegister}>
        Don't have an account? Register
      </button>
    </div>
  );
}

export default Login;
