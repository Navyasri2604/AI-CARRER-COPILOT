import React, { useState } from 'react';
import { UploadCloud, CheckCircle, FileText } from 'lucide-react';

const ResumeUpload = () => {
  const [file, setFile] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [result, setResult] = useState(null);

  const handleDrop = (e) => {
    e.preventDefault();
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      setFile(e.dataTransfer.files[0]);
    }
  };

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const analyze = () => {
    if (!file) return;
    setAnalyzing(true);
    // Simulate API call
    setTimeout(() => {
      setAnalyzing(false);
      setResult({
        score: 75,
        skills: ['React', 'JavaScript', 'Node.js'],
        strengths: ['Good format', 'Clear skills section'],
        weaknesses: ['Lack of quantifiable achievements']
      });
    }, 2000);
  };

  return (
    <div className="animate-fade">
      <div className="mb-6">
        <h1 className="section-title">Resume Analysis</h1>
        <p className="section-subtitle">Upload your resume for AI-powered feedback.</p>
      </div>

      {!result ? (
        <div className="card max-w-2xl mx-auto">
          <div 
            className="file-upload-area"
            onDragOver={(e) => e.preventDefault()}
            onDrop={handleDrop}
          >
            {analyzing ? (
              <div className="py-8">
                <div className="loading-spinner mx-auto mb-4"></div>
                <h3 className="font-bold mb-2">Analyzing your resume...</h3>
                <p className="text-muted text-sm">Extracting skills and evaluating format.</p>
              </div>
            ) : file ? (
              <div className="py-8">
                <div className="w-16 h-16 bg-violet-500/10 text-violet-500 rounded-full flex-center mx-auto mb-4">
                  <FileText size={32} />
                </div>
                <h3 className="font-bold mb-2">{file.name}</h3>
                <p className="text-muted text-sm mb-6">{(file.size / 1024 / 1024).toFixed(2)} MB</p>
                <div className="flex justify-center gap-3">
                  <button className="btn btn-ghost" onClick={() => setFile(null)}>Cancel</button>
                  <button className="btn btn-primary" onClick={analyze}>Analyze Resume</button>
                </div>
              </div>
            ) : (
              <div className="py-8">
                <UploadCloud className="file-upload-icon mx-auto" />
                <h3 className="file-upload-title">Drag & Drop your resume</h3>
                <p className="file-upload-sub mb-6">Supports PDF and DOCX formats up to 5MB</p>
                <input 
                  type="file" 
                  id="resume-upload" 
                  className="hidden" 
                  style={{display: 'none'}}
                  accept=".pdf,.docx"
                  onChange={handleFileChange}
                />
                <button 
                  className="btn btn-secondary" 
                  onClick={() => document.getElementById('resume-upload').click()}
                >
                  Browse Files
                </button>
              </div>
            )}
          </div>
        </div>
      ) : (
        <div className="grid grid-2">
          <div className="card">
            <h3 className="font-bold mb-4">Analysis Results</h3>
            <div className="flex items-center gap-6 mb-6">
              <div className="score-circle">
                {result.score}
              </div>
              <div>
                <h4 className="font-bold text-lg">Good potential</h4>
                <p className="text-muted text-sm">Your resume passes standard ATS checks but could use more impact metrics.</p>
              </div>
            </div>
            
            <div className="mb-4">
              <h4 className="font-bold text-sm mb-2 text-violet">Detected Skills</h4>
              <div className="flex flex-wrap">
                {result.skills.map(s => <span key={s} className="tag">{s}</span>)}
              </div>
            </div>
          </div>
          
          <div className="card">
            <h3 className="font-bold mb-4 text-lime">Strengths</h3>
            <ul className="flex flex-col gap-2 mb-6">
              {result.strengths.map((s, i) => (
                <li key={i} className="flex gap-2 items-start text-sm">
                  <CheckCircle size={16} className="text-lime shrink-0 mt-0.5" /> {s}
                </li>
              ))}
            </ul>
            
            <h3 className="font-bold mb-4 text-orange">Areas to Improve</h3>
            <ul className="flex flex-col gap-2">
              {result.weaknesses.map((s, i) => (
                <li key={i} className="flex gap-2 items-start text-sm">
                  <div className="w-4 h-4 rounded-full bg-orange-500/20 text-orange-500 flex-center shrink-0 mt-0.5 text-[10px] font-bold">!</div> {s}
                </li>
              ))}
            </ul>
            
            <button className="btn btn-primary w-full mt-6" onClick={() => {setResult(null); setFile(null);}}>
              Analyze Another Resume
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ResumeUpload;
