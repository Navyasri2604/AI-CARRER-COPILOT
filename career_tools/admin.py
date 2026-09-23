from django.contrib import admin
from .models import ChatConversation, ChatMessage, GeneratedAsset, JobApplication, JobMatch, ProjectRecommendation

@admin.register(JobMatch)
class JobMatchAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'score', 'user', 'created_at')
    search_fields = ('title', 'company', 'job_description')
    list_filter = ('created_at',)

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('company', 'job_title', 'status', 'user', 'created_at')
    search_fields = ('company', 'job_title')
    list_filter = ('status',)

admin.site.register(ProjectRecommendation)
admin.site.register(GeneratedAsset)
admin.site.register(ChatConversation)
admin.site.register(ChatMessage)
