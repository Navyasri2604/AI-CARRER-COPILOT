from django.contrib.auth.models import User
from django.db import models
class Roadmap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roadmaps')
    role = models.CharField(max_length=100)
    missing_skills = models.JSONField(default=list)
    content = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

class RoadmapTask(models.Model):
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=30, default='Intermediate')
    estimated_time = models.CharField(max_length=60, blank=True)
    resources = models.JSONField(default=list)
    completed = models.BooleanField(default=False)
