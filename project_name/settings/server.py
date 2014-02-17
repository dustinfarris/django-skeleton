from os import pardir
from os.path import abspath, dirname, join


# Assets

BASE_DIR = abspath(join(dirname(__file__), pardir, pardir))
STATIC_ROOT = join(BASE_DIR, 'static')
MEDIA_ROOT = join(BASE_DIR, 'media')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


# Environment

DEBUG = True
TEMPLATE_DEBUG = True


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
    'gunicorn',
    '{{ project_name }}',
    'south',
)
AUTH_USER_MODEL = '{{ project_name }}.User'
ROOT_URLCONF = '{{ project_name }}.urls'


# Security

SESSION_COOKIE_DOMAIN = ''
SECRET_KEY = '{{ secret_key }}'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': 'web',
    },
}


# Caching

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },
}


# Task queuing

CELERY_DISABLE_RATE_LIMITS = True
CELERY_ALWAYS_EAGER = True  # Set to False in production
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_RESULT_BACKEND = 'redis://'


# Internationalization

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Server

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# Email

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = ''
EMAIL_HOST_USER = 'noreply@{{ project_name }}.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = '[{{ project_name }}] '
DEFAULT_FROM_EMAIL = 'noreply@{{ project_name }}.com'


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
