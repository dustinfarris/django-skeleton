from settings import *


# Rackspace CDN
MEDIA_URL = 'http://cdn.{{ project_name }}.com/'
STATIC_URL = 'http://cdn.{{ project_name }}.com/static/'

RAX = {
  'USERNAME': '',
  'API_KEY': '',
  'REGION': 'ORD',
  'CONTAINER': '{{ project_name }}'}

DEFAULT_FILE_STORAGE = 'rax.storage.RaxStorage'
COMPRESS_URL = STATIC_URL

# Raven/Sentry DSN
# RAVEN_CONFIG = {'dsn': 'http://xxxxxxxx:yyyyyyy@sentry.myserver.com/z'}
