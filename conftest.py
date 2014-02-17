import os

from django.conf import settings


def pytest_configure(config):
    if not settings.configured:
        os.environ['DJANGO_SETTINGS_MODULE'] = '{{ project_name }}.settings'

    settings.DATABASES['default'].update({'ENGINE': 'django.db.backends.sqlite3'})
    settings.PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
    settings.INSTALLED_APPS = tuple(settings.INSTALLED_APPS) + ('tests',)
