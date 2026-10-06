from django.urls import path
from .views import skill_gap
urlpatterns = [path('', skill_gap, name='skill-gap')]
