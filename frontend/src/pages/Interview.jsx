import React, { useState } from 'react';
import { MessageSquare, Mic, Send } from 'lucide-react';

const Interview = () => {
  const [messages, setMessages] = useState([
    { role: 'assistant', text: "Hello! I'm your AI Interviewer. Today we'll be doing a technical behavioral interview for the Software Engineer role. Tell me about a time you had to resolve a difficult bug in production." }
  ]);
  const [input, setInput] = useState('');

  const handleSend = (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    
    setMessages([...messages, { role: 'user', text: input }]);
    setInput('');
    
    // Simulate AI response
    setTimeout(() => {
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        text: "That's a good example using the STAR method. I notice you mentioned debugging a memory leak. Could you elaborate on exactly which profiling tools you used and how you identified the root cause?" 
      }]);
    }, 1500);
  };

  return (
    <div className="animate-fade flex flex-col h-[calc(100vh-100px)]">
      <div className="mb-4">
        <h1 className="section-title">Interview Prep</h1>
        <p className="section-subtitle">Practice with your AI copilot</p>
      </div>

      <div className="card flex-1 flex flex-col overflow-hidden p-0 relative">
        <div className="bg-secondary p-4 border-b border-border flex-between">
          <div className="flex gap-3 items-center">
            <div className="w-10 h-10 rounded-full bg-gradient-main flex-center">
              <MessageSquare size={20} className="text-white" />
            </div>
            <div>
              <div className="font-bold text-sm">Technical Behavioral</div>
              <div className="text-xs text-lime">● Online</div>
            </div>
          </div>
          <button className="btn btn-ghost btn-sm">End Session</button>
        </div>
        
        <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-4 bg-bg-primary">
          {messages.map((msg, i) => (
            <div key={i} className={`max-w-[80%] p-4 rounded-2xl text-sm leading-relaxed ${
              msg.role === 'user' 
                ? 'bg-gradient-main text-white self-end rounded-br-sm' 
                : 'bg-card border border-border text-text-primary self-start rounded-bl-sm'
            }`}>
              {msg.text}
            </div>
          ))}
        </div>
        
        <div className="p-4 bg-secondary border-t border-border">
          <form onSubmit={handleSend} className="flex gap-2">
            <button type="button" className="w-12 h-12 rounded-lg bg-card border border-border flex-center text-muted hover:text-cyan transition-colors">
              <Mic size={20} />
            </button>
            <input 
              type="text" 
              className="flex-1 bg-card border border-border rounded-lg px-4 text-sm text-text-primary focus:border-violet-500 outline-none"
              placeholder="Type your answer..."
              value={input}
              onChange={e => setInput(e.target.value)}
            />
            <button type="submit" className="w-12 h-12 rounded-lg bg-gradient-main text-white flex-center hover:opacity-90">
              <Send size={20} className="ml-1" />
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Interview;
