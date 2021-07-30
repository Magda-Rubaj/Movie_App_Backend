import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Movie_App.settings')

app = Celery('Movie_App')

app.config_from_object('django.conf:settings', namespace='CELERY')
