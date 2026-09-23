from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from resume_analysis.models import ResumeAnalysis
from skill_gap.data import ROLE_SKILLS
from .utils import generate_roadmap
from .models import RoadmapTask

@login_required
def roadmap(request):
    role = request.GET.get('role') or getattr(getattr(request.user, 'profile', None), 'target_role', 'Software Engineer')
    required = ROLE_SKILLS.get(role, ROLE_SKILLS['Software Engineer'])
    latest = ResumeAnalysis.objects.filter(user=request.user).first()
    existing = {skill.lower() for skill in (latest.skills if latest else [])}
    missing = [skill for skill in required if skill.lower() not in existing]
    content = generate_roadmap(role, missing, request.user) if request.GET.get('generate') else None
    latest = request.user.roadmaps.order_by('-created_at').first()
    return render(request, 'roadmap/index.html', {'roles': ROLE_SKILLS, 'role': role, 'missing': missing, 'content': content, 'tasks': latest.tasks.all() if latest else []})

@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(RoadmapTask, pk=task_id, roadmap__user=request.user)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save(update_fields=['completed'])
    return redirect('roadmap')
