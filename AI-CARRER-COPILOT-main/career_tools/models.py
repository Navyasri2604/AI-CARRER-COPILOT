from django.contrib.auth.models import User
from django.db import models

class JobMatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_matches')
    title = models.CharField(max_length=160, blank=True)
    company = models.CharField(max_length=160, blank=True)
    job_description = models.TextField()
    resume = models.ForeignKey('resume_analysis.ResumeAnalysis', on_delete=models.SET_NULL, null=True, blank=True)
    score = models.PositiveSmallIntegerField(default=0)
    breakdown = models.JSONField(default=dict)
    matched_skills = models.JSONField(default=list)
    missing_skills = models.JSONField(default=list)
    keywords = models.JSONField(default=list)
    recommendations = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

class JobApplication(models.Model):
    STATUSES = [('Wishlist', 'Wishlist'), ('Applied', 'Applied'), ('Assessment', 'Assessment'), ('Interview', 'Interview'), ('Offer', 'Offer'), ('Rejected', 'Rejected')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    company = models.CharField(max_length=160)
    job_title = models.CharField(max_length=160)
    location = models.CharField(max_length=120, blank=True)
    job_url = models.URLField(blank=True)
    date_applied = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUSES, default='Wishlist')
    notes = models.TextField(blank=True)
    interview_date = models.DateField(null=True, blank=True)
    salary_range = models.CharField(max_length=80, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_recommendations')
    name = models.CharField(max_length=180)
    difficulty = models.CharField(max_length=30)
    skills = models.JSONField(default=list)
    problem_statement = models.TextField()
    features = models.JSONField(default=list)
    tech_stack = models.JSONField(default=list)
    expected_outcome = models.TextField()
    portfolio_value = models.TextField()
    status = models.CharField(max_length=20, default='Saved')
    created_at = models.DateTimeField(auto_now_add=True)

class GeneratedAsset(models.Model):
    TYPES = [('cover_letter', 'Cover letter'), ('email', 'Email'), ('resume_bullets', 'Resume bullets'), ('linkedin', 'LinkedIn profile')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='generated_assets')
    asset_type = models.CharField(max_length=30, choices=TYPES)
    prompt_context = models.JSONField(default=dict)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ChatConversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_conversations')
    title = models.CharField(max_length=160, default='Career conversation')
    created_at = models.DateTimeField(auto_now_add=True)

class ChatMessage(models.Model):
    conversation = models.ForeignKey(ChatConversation, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=20, choices=[('user', 'User'), ('assistant', 'Assistant')])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
