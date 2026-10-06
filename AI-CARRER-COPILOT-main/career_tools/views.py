import re
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import redirect, render
from resume_analysis.models import ResumeAnalysis
from skill_gap.data import ROLE_SKILLS
from ai_service import keyword_matches, local_asset, local_chat_reply, similarity_score
from .forms import JobApplicationForm, JobMatchForm
from .models import ChatConversation, ChatMessage, GeneratedAsset, JobApplication, JobMatch, ProjectRecommendation

COMMON_TERMS = ['python', 'sql', 'javascript', 'django', 'java', 'docker', 'kubernetes', 'aws', 'azure', 'git', 'tensorflow', 'pytorch', 'react', 'machine learning', 'statistics', 'excel', 'tableau', 'power bi', 'rest api', 'testing', 'communication', 'leadership']

def analyze_description(description, skills):
    lower = description.lower()
    required = [term.title() for term in COMMON_TERMS if term in lower]
    known = {skill.lower() for skill in skills}
    matched = [term for term in required if term.lower() in known]
    missing = [term for term in required if term not in matched]
    skill_score = round(len(matched) / len(required) * 100) if required else 0
    score = round((skill_score * 0.7) + (similarity_score(description, ' '.join(skills)) * 0.3)) if required else 0
    return {'score': score, 'breakdown': {'skills': skill_score, 'experience': min(100, score + 5), 'education': 70 if 'degree' in lower or 'bachelor' in lower else 50, 'keywords': min(100, score + 10), 'tools': round(len(matched) / max(1, len(required)) * 100)}, 'matched_skills': matched, 'missing_skills': missing, 'keywords': required[:12], 'recommendations': [f'Add evidence for {skill} in a project or experience bullet.' for skill in missing[:5]]}

@login_required
def job_match(request):
    latest = ResumeAnalysis.objects.filter(user=request.user).first()
    form = JobMatchForm(request.POST or None)
    result = None
    if request.method == 'POST' and form.is_valid():
        match = form.save(commit=False)
        match.user = request.user
        match.resume = latest
        result = analyze_description(match.job_description, latest.skills if latest else [])
        for key, value in result.items(): setattr(match, key, value)
        match.save()
        messages.success(request, 'Job match analyzed and saved to your history.')
        return render(request, 'career_tools/matcher.html', {'form': JobMatchForm(), 'result': result, 'match': match, 'history': JobMatch.objects.filter(user=request.user)[:8]})
    return render(request, 'career_tools/matcher.html', {'form': form, 'history': JobMatch.objects.filter(user=request.user)[:8]})

@login_required
def applications(request):
    form = JobApplicationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        application = form.save(commit=False)
        application.user = request.user
        application.save()
        messages.success(request, 'Application added to your tracker.')
        return redirect('applications')
    items = JobApplication.objects.filter(user=request.user).order_by('-created_at')
    counts = {row['status']: row['total'] for row in items.values('status').annotate(total=Count('id'))}
    status_counts = [{'label': label, 'count': counts.get(value, 0)} for value, label in JobApplication.STATUSES]
    return render(request, 'career_tools/applications.html', {'form': form, 'applications': items, 'status_counts': status_counts})

@login_required
def project_recommendations(request):
    role = getattr(getattr(request.user, 'profile', None), 'target_role', 'Software Engineer')
    latest = ResumeAnalysis.objects.filter(user=request.user).first()
    missing = [skill for skill in ROLE_SKILLS.get(role, ROLE_SKILLS['Software Engineer']) if skill.lower() not in {item.lower() for item in (latest.skills if latest else [])}]
    projects = ProjectRecommendation.objects.filter(user=request.user)
    if request.GET.get('save'):
        ProjectRecommendation.objects.get_or_create(user=request.user, name='AI Career Portfolio Builder', defaults={'difficulty': 'Intermediate', 'skills': missing[:5] or ['Python', 'Django'], 'problem_statement': 'Build a useful portfolio platform that turns career evidence into job-ready output.', 'features': ['Profile analysis', 'Progress tracking', 'Exportable portfolio'], 'tech_stack': ['Python', 'Django', 'SQLite'], 'expected_outcome': 'A deployed portfolio project with measurable user value.', 'portfolio_value': 'Demonstrates product thinking, backend architecture, and AI workflow design.'})
        messages.success(request, 'Project saved to your portfolio queue.')
        return redirect('projects')
    return render(request, 'career_tools/projects.html', {'projects': projects, 'role': role, 'missing': missing})

@login_required
def studio(request):
    asset_type = request.POST.get('asset_type', 'cover_letter') if request.method == 'POST' else 'cover_letter'
    content = None
    message = None
    if request.method == 'POST':
        context = request.POST.get('context', '').strip()
        if not context:
            message = 'Add context before generating your asset.'
        else:
            labels = {'cover_letter': 'a tailored cover letter', 'email': 'a professional recruiter email', 'resume_bullets': 'three ATS-friendly resume bullet points', 'linkedin': 'a truthful LinkedIn headline and About section'}
            content = local_asset(asset_type, context)
            GeneratedAsset.objects.create(user=request.user, asset_type=asset_type, prompt_context={'context': context}, content=content)
    return render(request, 'career_tools/studio.html', {'asset_type': asset_type, 'content': content, 'message': message, 'history': GeneratedAsset.objects.filter(user=request.user)[:10]})

@login_required
def assistant(request):
    conversation, _ = ChatConversation.objects.get_or_create(user=request.user, title='Career conversation')
    if request.method == 'POST':
        prompt = request.POST.get('message', '').strip()
        if prompt:
            ChatMessage.objects.create(conversation=conversation, role='user', content=prompt)
            profile = getattr(request.user, 'profile', None)
            latest = ResumeAnalysis.objects.filter(user=request.user).first()
            profile_text = f'{profile.target_role} {profile.bio} {profile.skills}' if profile else ''
            resume_text = latest.raw_text if latest else ''
            ChatMessage.objects.create(conversation=conversation, role='assistant', content=local_chat_reply(prompt, profile_text, resume_text))
    return render(request, 'career_tools/assistant.html', {'conversation': conversation, 'messages': conversation.messages.order_by('created_at')})
