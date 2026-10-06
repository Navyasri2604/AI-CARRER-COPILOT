import React, { useState } from 'react';
import { Outlet, NavLink, useNavigate } from 'react-router-dom';
import { LayoutDashboard, FileText, Map, User, LogOut, Menu, X, MessageSquare, Briefcase } from 'lucide-react';

const Layout = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('user');
    localStorage.removeItem('token');
    navigate('/');
  };

  const navItems = [
    { name: 'Dashboard', path: '/app/dashboard', icon: <LayoutDashboard size={20} /> },
    { name: 'Resume Analysis', path: '/app/resume', icon: <FileText size={20} /> },
    { name: 'Career Roadmap', path: '/app/roadmap', icon: <Map size={20} /> },
    { name: 'Interview Prep', path: '/app/interview', icon: <MessageSquare size={20} /> },
  ];

  return (
    <div className="app-layout">
      {/* Mobile Header */}
      <div className="topbar" style={{ display: 'none' }}>
        <div className="flex gap-2 items-center">
          <button className="btn btn-ghost" onClick={() => setSidebarOpen(true)}>
            <Menu size={24} />
          </button>
          <span className="font-bold text-lg">AI Copilot</span>
        </div>
      </div>

      {/* Sidebar */}
      <aside className={`sidebar ${sidebarOpen ? 'open' : ''}`}>
        <div className="sidebar-logo flex-between">
          <div className="flex gap-2 items-center">
            <div className="logo-icon">AI</div>
            <div>
              <div className="logo-text">Career Copilot</div>
              <div className="logo-sub">Your personal advisor</div>
            </div>
          </div>
          <button className="btn btn-ghost p-1" style={{ display: 'none' }} onClick={() => setSidebarOpen(false)}>
            <X size={20} />
          </button>
        </div>

        <nav className="sidebar-nav">
          <div className="nav-section-label">Tools</div>
          {navItems.map((item) => (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}
              onClick={() => setSidebarOpen(false)}
            >
              <div className="nav-icon">{item.icon}</div>
              {item.name}
            </NavLink>
          ))}
        </nav>

        <div className="sidebar-footer">
          <div className="user-info flex-between mb-2">
            <div className="flex gap-2 items-center">
              <div className="user-avatar">
                <User size={18} />
              </div>
              <div>
                <div className="user-name">User</div>
                <div className="user-role">Software Engineer</div>
              </div>
            </div>
            <button className="btn btn-ghost p-1" onClick={handleLogout} title="Logout">
              <LogOut size={16} />
            </button>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="main-content">
        <div className="page-content">
          <Outlet />
        </div>
      </main>
    </div>
  );
};

export default Layout;
