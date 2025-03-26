import { useState } from 'react';
import './Register.css';

function Register({ onNavigateToLogin }: { onNavigateToLogin: () => void }) {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    firstName: '',
    lastName: '',
    role: '3', // Default to 'User'
  });
  const [message, setMessage] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:8000/api/register/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        setMessage('Registration successful!');
      } else {
        const errorData = await response.json();
        setMessage(errorData.error || 'Registration failed.');
      }
    } catch (error) {
      setMessage('An error occurred. Please try again.');
    }
  };

  return (
    <div className="register-container">
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="firstName" placeholder="First Name" value={formData.firstName} onChange={handleChange} required />
        <input type="text" name="lastName" placeholder="Last Name" value={formData.lastName} onChange={handleChange} required />
        <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
        <input type="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} required />
        <select name="role" value={formData.role} onChange={handleChange}>
          <option value="3">User</option>
          <option value="2">Staff</option>
          <option value="1">Admin</option>
        </select>
        <button type="submit">Register</button>
      </form>
      {message && <p>{message}</p>}
      <button className="navigate-button" onClick={onNavigateToLogin}>
        Already have an account? Login
      </button>
    </div>
  );
}

export default Register;
