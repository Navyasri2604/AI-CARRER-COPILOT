from django import forms
from .models import JobApplication, JobMatch

class JobMatchForm(forms.ModelForm):
    class Meta:
        model = JobMatch
        fields = ('title', 'company', 'job_description')
        widgets = {'job_description': forms.Textarea(attrs={'rows': 12, 'placeholder': 'Paste the full job description here...'})}

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ('company', 'job_title', 'location', 'job_url', 'date_applied', 'status', 'notes', 'interview_date', 'salary_range')
        widgets = {'date_applied': forms.DateInput(attrs={'type': 'date'}), 'interview_date': forms.DateInput(attrs={'type': 'date'}), 'notes': forms.Textarea(attrs={'rows': 3})}
