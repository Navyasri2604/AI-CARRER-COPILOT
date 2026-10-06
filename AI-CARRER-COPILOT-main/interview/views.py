from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import InterviewSession
from .utils import evaluate_answer, question_for

@login_required
def interview(request):
    role = getattr(getattr(request.user, 'profile', None), 'target_role', 'Software Engineer')
    category = request.GET.get('category', 'Technical')
    level = request.GET.get('level', 'Intermediate')
    question = question_for(role, category, level)
    feedback = None
    if request.method == 'POST':
        answer = request.POST.get('answer', '').strip()
        feedback = evaluate_answer(role, question, answer)
        InterviewSession.objects.create(user=request.user, role=role, category=category, question=question, answer=answer, score=feedback.get('score', 0), feedback=feedback)
    return render(request, 'interview/index.html', {'question': question, 'role': role, 'category': category, 'level': level, 'feedback': feedback})
