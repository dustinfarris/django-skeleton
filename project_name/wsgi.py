import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')

from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
from django.core.wsgi import WSGIHandler

application = Sentry(WSGIHandler())
