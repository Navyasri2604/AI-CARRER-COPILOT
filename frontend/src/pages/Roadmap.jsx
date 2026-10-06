import React from 'react';
import { Map, CheckCircle } from 'lucide-react';

const Roadmap = () => {
  const steps = [
    { title: 'Core Python & Django', duration: 'Weeks 1-2', status: 'completed' },
    { title: 'RESTful APIs & DRF', duration: 'Weeks 3-4', status: 'current' },
    { title: 'React Frontend Integration', duration: 'Weeks 5-6', status: 'pending' },
    { title: 'Deployment & CI/CD', duration: 'Weeks 7-8', status: 'pending' }
  ];

  return (
    <div className="animate-fade">
      <div className="mb-6">
        <h1 className="section-title">Career Roadmap</h1>
        <p className="section-subtitle">Your personalized learning path to Software Engineer.</p>
      </div>

      <div className="card max-w-3xl mx-auto">
        <div className="flex items-center gap-4 mb-8 pb-6 border-b border-border">
          <div className="w-12 h-12 bg-lime-500/10 text-lime-500 rounded-xl flex-center">
            <Map size={24} />
          </div>
          <div>
            <h3 className="font-bold text-lg">Full-Stack Developer Track</h3>
            <p className="text-muted text-sm">Estimated completion: 2 months</p>
          </div>
          <div className="ml-auto">
            <span className="badge badge-lime">25% Complete</span>
          </div>
        </div>

        <div className="flex flex-col gap-6 relative">
          <div className="absolute left-[15px] top-4 bottom-4 w-0.5 bg-border z-0"></div>
          
          {steps.map((step, idx) => (
            <div key={idx} className="flex gap-4 relative z-10">
              <div className={`w-8 h-8 rounded-full flex-center shrink-0 border-4 border-card ${
                step.status === 'completed' ? 'bg-lime-500 text-bg-primary' : 
                step.status === 'current' ? 'bg-violet-500 text-white' : 
                'bg-secondary text-muted border-border'
              }`}>
                {step.status === 'completed' ? <CheckCircle size={14} /> : (idx + 1)}
              </div>
              <div className={`flex-1 p-4 rounded-lg border ${
                step.status === 'current' ? 'border-violet-500/50 bg-violet-500/5' : 'border-border bg-secondary'
              }`}>
                <div className="flex-between mb-2">
                  <h4 className={`font-bold ${step.status === 'current' ? 'text-violet' : ''}`}>{step.title}</h4>
                  <span className="text-xs text-muted">{step.duration}</span>
                </div>
                <p className="text-sm text-muted">Complete the associated projects and readings to advance to the next step.</p>
                {step.status === 'current' && (
                  <button className="btn btn-primary btn-sm mt-4">Continue Learning</button>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Roadmap;
