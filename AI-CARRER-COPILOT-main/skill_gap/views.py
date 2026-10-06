from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from resume_analysis.models import ResumeAnalysis
from .data import ROLE_SKILLS

@login_required
def skill_gap(request):
    role = request.GET.get('role') or getattr(getattr(request.user, 'profile', None), 'target_role', 'Software Engineer')
    role = role if role in ROLE_SKILLS else 'Software Engineer'
    latest = ResumeAnalysis.objects.filter(user=request.user).first()
    existing = latest.skills if latest else []
    required = ROLE_SKILLS[role]
    existing_lower = {item.lower() for item in existing}
    matched = [item for item in required if item.lower() in existing_lower]
    missing = [item for item in required if item not in matched]
    return render(request, 'skill_gap/index.html', {'roles': ROLE_SKILLS, 'role': role, 'required': required, 'matched': matched, 'missing': missing, 'readiness': round(len(matched) / len(required) * 100) if required else 0})
