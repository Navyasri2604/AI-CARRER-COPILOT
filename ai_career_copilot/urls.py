from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('resume/', include('resume_analysis.urls')),
    path('skills/', include('skill_gap.urls')),
    path('roadmap/', include('roadmap.urls')),
    path('recommendations/', include('recommendations.urls')),
    path('interview/', include('interview.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('career/', include('career_tools.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
