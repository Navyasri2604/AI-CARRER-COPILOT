from django.urls import path
from .views import resume_detail, upload_resume
urlpatterns = [path('', upload_resume, name='resume-upload'), path('<int:pk>/', resume_detail, name='resume-detail')]
