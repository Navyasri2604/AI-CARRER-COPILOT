from django.contrib.auth.models import User
from django.db import models
class InterviewSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interviews')
    role = models.CharField(max_length=100)
    category = models.CharField(max_length=40, default='Technical')
    question = models.TextField()
    answer = models.TextField(blank=True)
    score = models.PositiveSmallIntegerField(default=0)
    feedback = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
