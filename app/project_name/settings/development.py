from {{ project_name }}.settings.common import *


SESSION_COOKIE_DOMAIN = ''
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ENVIRONMENT = 'develop'
