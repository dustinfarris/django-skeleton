import os

from celery import Celery

from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')

app = Celery('{{ project_name }}')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
