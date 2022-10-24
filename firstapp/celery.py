import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstapp.settings.dev')
celery = Celery('firstapp')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()

