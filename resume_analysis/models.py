from django.contrib.auth.models import User
from django.db import models

class ResumeAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume_analyses')
    file = models.FileField(upload_to='resumes/')
    raw_text = models.TextField(blank=True)
    skills = models.JSONField(default=list)
    education = models.JSONField(default=list)
    projects = models.JSONField(default=list)
    certifications = models.JSONField(default=list)
    experience = models.JSONField(default=list)
    achievements = models.JSONField(default=list)
    languages = models.JSONField(default=list)
    tools = models.JSONField(default=list)
    soft_skills = models.JSONField(default=list)
    score = models.PositiveSmallIntegerField(default=0)
    score_breakdown = models.JSONField(default=dict)
    strengths = models.JSONField(default=list)
    weaknesses = models.JSONField(default=list)
    recommendations = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def skill_count(self): return len(self.skills)
