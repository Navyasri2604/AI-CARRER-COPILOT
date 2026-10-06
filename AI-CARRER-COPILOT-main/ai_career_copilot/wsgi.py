import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_career_copilot.settings')
application = get_wsgi_application()
