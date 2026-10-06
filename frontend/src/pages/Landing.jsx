import React from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, Play, FileText, Map, MessageSquare } from 'lucide-react';

const Landing = () => {
  return (
    <div className="landing">
      <nav className="landing-nav">
        <Link to="/" className="logo">
          <div className="logo-icon" style={{ width: '32px', height: '32px', background: 'var(--gradient-main)', borderRadius: '8px', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 'bold' }}>AI</div>
          Career Copilot
        </Link>
        <div className="flex gap-3">
          <Link to="/login" className="btn btn-ghost">Log in</Link>
          <Link to="/register" className="btn btn-primary">Get Started</Link>
        </div>
      </nav>

      <section className="hero-section">
        <div className="container">
          <div className="hero-content">
            <div className="hero-eyebrow">Your career, intelligently mapped</div>
            <h1 className="hero-title">Turn your next career move into a <em>clear plan.</em></h1>
            <p className="hero-sub">AI Career Copilot reads your real experience, finds your highest-leverage skills, and builds a local, practical path to your next role.</p>
            
            <div className="hero-actions">
              <Link to="/register" className="btn btn-primary btn-lg">
                Build my career plan <ArrowRight size={18} />
              </Link>
              <a href="#features" className="btn btn-secondary btn-lg">
                See how it works <Play size={18} />
              </a>
            </div>
          </div>
        </div>
      </section>

      <section id="features" className="features-section">
        <div className="container">
          <div className="section-label">Features</div>
          <h2>Every step, connected.</h2>
          <p className="section-sub">One calm workspace for the work that usually takes ten scattered tabs.</p>
          
          <div className="feature-grid">
            <div className="feature-card">
              <div className="feature-icon-wrap" style={{ background: 'rgba(0,212,255,0.1)', color: 'var(--accent-cyan)' }}>
                <FileText />
              </div>
              <h3>See your signal</h3>
              <p>Upload a PDF or DOCX resume and get an honest, skill-by-skill snapshot of what you already bring.</p>
            </div>
            
            <div className="feature-card">
              <div className="feature-icon-wrap" style={{ background: 'rgba(132,204,22,0.1)', color: 'var(--accent-lime)' }}>
                <Map />
              </div>
              <h3>Know what to learn</h3>
              <p>Compare your profile to your target role and get a focused 30/60/90 day plan with tracked tasks.</p>
            </div>
            
            <div className="feature-card">
              <div className="feature-icon-wrap" style={{ background: 'rgba(249,115,22,0.1)', color: 'var(--accent-orange)' }}>
                <MessageSquare />
              </div>
              <h3>Practice with pressure</h3>
              <p>Run tailored interview drills and get transparent rule-based feedback on every answer.</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Landing;
