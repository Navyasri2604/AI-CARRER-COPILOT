from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    ROLES = [(role, role) for role in ['AI Engineer', 'Machine Learning Engineer', 'Data Analyst', 'Data Scientist', 'Software Engineer', 'Java Developer', 'Python Developer', 'QA Automation Engineer', 'ServiceNow Developer', 'Business Analyst', 'Cloud Engineer', 'DevOps Engineer', 'Cybersecurity Analyst']]
    EXPERIENCE_LEVELS = [('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    target_role = models.CharField(max_length=80, choices=ROLES, default='Software Engineer')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    full_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=120, blank=True)
    current_role = models.CharField(max_length=120, blank=True)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVELS, default='Beginner')
    education = models.TextField(blank=True)
    skills = models.JSONField(default=list, blank=True)
    preferred_location = models.CharField(max_length=120, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} profile'
