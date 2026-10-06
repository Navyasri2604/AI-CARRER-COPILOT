from django.urls import path
from .views import applications, assistant, job_match, project_recommendations, studio

urlpatterns = [
    path('matcher/', job_match, name='job-matcher'),
    path('applications/', applications, name='applications'),
    path('projects/', project_recommendations, name='projects'),
    path('studio/', studio, name='ai-studio'),
    path('assistant/', assistant, name='assistant'),
]
