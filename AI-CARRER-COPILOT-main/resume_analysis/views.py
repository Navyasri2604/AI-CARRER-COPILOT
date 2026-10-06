from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ResumeUploadForm
from .models import ResumeAnalysis
from .utils import extract_resume_data

@login_required
def upload_resume(request):
    form = ResumeUploadForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        analysis = form.save(commit=False)
        analysis.user = request.user
        try:
            data = extract_resume_data(request.FILES['file'])
        except Exception:
            form.add_error('file', 'Please upload a valid, readable PDF resume.')
        else:
            for key, value in data.items(): setattr(analysis, key, value)
            analysis.save()
            return redirect('resume-detail', analysis.pk)
    return render(request, 'resume_analysis/upload.html', {'form': form})

@login_required
def resume_detail(request, pk):
    analysis = get_object_or_404(ResumeAnalysis, pk=pk, user=request.user)
    return render(request, 'resume_analysis/detail_clean.html', {'analysis': analysis})
