from {{ project_name }}.settings.settings import *


# Rackspace CDN
MEDIA_URL = 'http://cdn.{{ project_name }}.com/'
STATIC_URL = 'http://cdn.{{ project_name }}.com/static/'

COMPRESS_URL = STATIC_URL

# Raven/Sentry DSN
# RAVEN_CONFIG = {'dsn': 'http://xxxxxxxx:yyyyyyy@sentry.myserver.com/z'}
