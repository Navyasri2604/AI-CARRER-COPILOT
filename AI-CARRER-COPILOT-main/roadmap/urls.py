from django.urls import path
from .views import roadmap, toggle_task
urlpatterns = [path('', roadmap, name='roadmap'), path('tasks/<int:task_id>/toggle/', toggle_task, name='toggle-roadmap-task')]
