import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { TrendingUp, FileText, Map, MessageSquare, ArrowRight, Zap, Target } from 'lucide-react';
import api from '../api';

const Dashboard = () => {
  const [data, setData] = useState({
    role: 'Software Engineer',
    readiness: 65,
    resume_count: 1,
    roadmap_count: 1,
    recent_interviews: [],
    loading: false
  });

  // Example frontend simulation for now, to be hooked to API later
  useEffect(() => {
    // If backend was ready for json:
    // api.get('/dashboard/data').then(res => setData({...data, ...res.data}));
  }, []);

  return (
    <div className="animate-fade">
      <div className="mb-6 flex-between">
        <div>
          <h1 className="section-title">Dashboard</h1>
          <p className="section-subtitle">Welcome back. Here is your career overview.</p>
        </div>
        <Link to="/app/resume" className="btn btn-primary">
          <Zap size={16} /> New Analysis
        </Link>
      </div>

      <div className="grid grid-4 mb-6">
        <div className="stat-card">
          <div className="flex-between mb-4">
            <div className="stat-icon cyan mb-0">
              <Target size={24} />
            </div>
            <div className="badge badge-cyan">{data.role}</div>
          </div>
          <div className="stat-value">{data.readiness}%</div>
          <div className="stat-label">Role Readiness Score</div>
        </div>

        <div className="stat-card">
          <div className="stat-icon violet">
            <FileText size={24} />
          </div>
          <div className="stat-value">{data.resume_count}</div>
          <div className="stat-label">Resumes Analyzed</div>
        </div>

        <div className="stat-card">
          <div className="stat-icon lime">
            <Map size={24} />
          </div>
          <div className="stat-value">{data.roadmap_count}</div>
          <div className="stat-label">Active Roadmaps</div>
        </div>

        <div className="stat-card">
          <div className="stat-icon pink">
            <TrendingUp size={24} />
          </div>
          <div className="stat-value">{data.recent_interviews.length}</div>
          <div className="stat-label">Practice Sessions</div>
        </div>
      </div>

      <div className="grid grid-2">
        <div className="card">
          <div className="flex-between mb-4">
            <h3 className="font-bold">Next Steps</h3>
          </div>
          
          <div className="flex flex-col gap-3">
            <div className="p-3 bg-secondary rounded-lg border border-border flex-between">
              <div className="flex gap-3 items-center">
                <div className="w-8 h-8 rounded-full bg-violet-500/20 text-violet-500 flex-center">1</div>
                <div>
                  <div className="font-bold text-sm">Update your Resume</div>
                  <div className="text-xs text-muted">Add measurable outcomes to your latest project.</div>
                </div>
              </div>
              <Link to="/app/resume" className="btn btn-ghost btn-sm">Go <ArrowRight size={14}/></Link>
            </div>
            
            <div className="p-3 bg-secondary rounded-lg border border-border flex-between">
              <div className="flex gap-3 items-center">
                <div className="w-8 h-8 rounded-full bg-lime-500/20 text-lime-500 flex-center">2</div>
                <div>
                  <div className="font-bold text-sm">Start Interview Prep</div>
                  <div className="text-xs text-muted">Practice behavioral questions for {data.role}.</div>
                </div>
              </div>
              <Link to="/app/interview" className="btn btn-ghost btn-sm">Go <ArrowRight size={14}/></Link>
            </div>
          </div>
        </div>
        
        <div className="card">
          <div className="flex-between mb-4">
            <h3 className="font-bold">Recent Interviews</h3>
            <Link to="/app/interview" className="text-sm text-cyan">View all</Link>
          </div>
          
          {data.recent_interviews.length > 0 ? (
            <div className="flex flex-col gap-3">
              {/* Loop interviews */}
            </div>
          ) : (
            <div className="text-center p-6 text-muted">
              <MessageSquare size={32} className="mx-auto mb-3 opacity-50" />
              <p>No practice sessions yet.</p>
              <Link to="/app/interview" className="btn btn-secondary mt-3">Start Practice</Link>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
