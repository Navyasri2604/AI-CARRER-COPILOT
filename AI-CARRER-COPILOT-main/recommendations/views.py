import json
from pathlib import Path
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from resume_analysis.models import ResumeAnalysis

@login_required
def recommendations(request):
    latest = ResumeAnalysis.objects.filter(user=request.user).first()
    missing = set(request.GET.getlist('missing'))
    if not missing:
        missing = set(request.GET.get('skills', '').split(',')) - {''}
    courses = json.loads((Path(__file__).parent / 'courses.json').read_text())
    matched = [course for course in courses if not missing or set(course['skills']) & missing]
    return render(request, 'recommendations/index.html', {'courses': matched, 'missing': missing})
