import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import Landing from './pages/Landing';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import ResumeUpload from './pages/ResumeUpload';
import Roadmap from './pages/Roadmap';
import Interview from './pages/Interview';

// Private Route Component
const PrivateRoute = ({ children }) => {
  const token = localStorage.getItem('token'); // In a real app, use Context/Redux
  // For demo purposes, if there is a 'user' item, consider them logged in
  const isAuthenticated = !!localStorage.getItem('user');
  
  return isAuthenticated ? children : <Navigate to="/login" replace />;
};

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        
        {/* Protected Routes inside Layout */}
        <Route path="/app" element={
          <PrivateRoute>
            <Layout />
          </PrivateRoute>
        }>
          <Route index element={<Navigate to="dashboard" replace />} />
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="resume" element={<ResumeUpload />} />
          <Route path="roadmap" element={<Roadmap />} />
          <Route path="interview" element={<Interview />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
