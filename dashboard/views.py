from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from interview.models import InterviewSession
from resume_analysis.models import ResumeAnalysis
from roadmap.models import Roadmap
from skill_gap.data import ROLE_SKILLS

@login_required
def dashboard(request):
    latest = ResumeAnalysis.objects.filter(user=request.user).first()
    role = getattr(getattr(request.user, 'profile', None), 'target_role', 'Software Engineer')
    required = ROLE_SKILLS.get(role, ROLE_SKILLS['Software Engineer'])
    existing = {s.lower() for s in (latest.skills if latest else [])}
    readiness = round(sum(s.lower() in existing for s in required) / len(required) * 100) if required else 0
    sessions = InterviewSession.objects.filter(user=request.user).order_by('created_at')
    return render(request, 'dashboard/main_dashboard.html', {'latest': latest, 'role': role, 'readiness': readiness, 'resume_count': ResumeAnalysis.objects.filter(user=request.user).count(), 'roadmap_count': Roadmap.objects.filter(user=request.user).count(), 'sessions': sessions, 'interview_scores': [s.score for s in sessions]})
