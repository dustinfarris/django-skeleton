from datetime import datetime

from {{ project_name }}.settings.common import *


ENVIRONMENT = 'test'

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
}
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
SESSION_COOKIE_DOMAIN = ''
CACHES['default']['KEY_PREFIX'] = 'test_%s' % datetime.now().timestamp()
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
LOGGING_CONFIG = None
