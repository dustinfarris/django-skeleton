from settings import *


DEBUG = False

DATABASES['default'] = {
  'ENGINE': 'django.db.backends.sqlite3',
  'TEST_NAME': ':memory:'}

PASSWORD_HASHERS = (
  'django.contrib.auth.hashers.MD5PasswordHasher',
  'django.contrib.auth.hashers.SHA1PasswordHasher')

SOUTH_TESTS_MIGRATE = False

TEST_RUNNER = 'redrover.RedRoverRunner'

COMPRESS_ENABLED = False

CACHES['default']['BACKEND'] = 'django.core.cache.backends.dummy.DummyCache'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = tuple(INSTALLED_APPS) + ('redrover', )

LOGGING = {
  'version': 1,
  'disable_existing_loggers': True,
  'handlers': {
    'null': {
      'level': 'DEBUG',
      'class': 'django.utils.log.NullHandler'},
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler'}},
  'loggers': {
    'django': {
      'handlers': ['null'],
      'propagate': False,
      'level': 'ERROR'},
    'django.db.backends': {
      'level': 'ERROR',
      'handlers': ['console'],
      'propagate': False},
    'django.request': {
      'handlers': ['null'],
      'propagate': True,
      'level': 'ERROR'}}}
