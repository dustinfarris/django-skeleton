# Django settings for the {{ project_name }} project.
from os.path import abspath, dirname, join


DEBUG = False
TEMPLATE_DEBUG = DEBUG

gettext = lambda s: s

PROJECT_DIR = abspath(join(dirname(__file__), "../../"))

ADMINS = (
  ('Your Name', 'you@example.org'),
)

MANAGERS = ADMINS

INTERNAL_IPS = ()

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': '{{ project_name }}',
    'USER': 'web',
    'PASSWORD': '',
    'HOST': '',
    'PORT': ''}}

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
LANGUAGES = (('en', gettext('English')),)
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (join(PROJECT_DIR, '{{ project_name }}', 'static'),)
STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  'compressor.finders.CompressorFinder')

SECRET_KEY = '{{ secret_key }}'

TEMPLATE_DIRS = (join(PROJECT_DIR, '{{ project_name }}', 'templates'))
TEMPLATE_LOADERS = (
  ('pyjade.ext.django.Loader', (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader')), )
TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.debug',
  'django.core.context_processors.i18n',
  'django.core.context_processors.media',
  'django.core.context_processors.static',
  'django.core.context_processors.tz',
  'django.core.context_processors.request',
  'django.contrib.messages.context_processors.messages',
  '{{ project_name }}.context_processors.google')

MIDDLEWARE_CLASSES = (
  'django.middleware.cache.UpdateCacheMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.middleware.cache.FetchFromCacheMiddleware',
  'raven.contrib.django.middleware.Sentry404CatchMiddleware')

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.admin',
  'django.contrib.admindocs',
  'compressor',
  'easy_thumbnails',
  'raven.contrib.django.raven_compat',
  'south')

CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    'LOCATION': '127.0.0.1:11211',
    'KEY_PREFIX': '{{ project_name }}',
    'TIMEOUT': 300,
    'VERSION': 1}}
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

# Google Analytics UA, e.g. UA-XXXXXXX
#GOOGLE_UA = ''

COMPRESS_OFFLINE = False
COMPRESS_CSS_HASHING_METHOD = 'hash'
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
COMPRESS_CSS_FILTERS = [
  'compressor.filters.css_default.CssAbsoluteFilter',
  'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter', ]
COMPRESS_PRECOMPILERS = (
  ('text/coffeescript', 'coffee --compile --stdio'),
  ('text/less', 'lessc {infile} {outfile}'),
  ('text/x-sass', 'sass {infile} {outfile}'),
  ('text/x-scss', 'sass --scss {infile} {outfile}'))

# Fabfile settings
# STAGING_SERVER_HOST = '12.12.12.12'
# STAGING_SERVER_USER = 'web'
# PRODUCTION_SERVER_HOST = '45.45.45.45'
# PRODUCTION_SERVER_USER = 'web'

LOGGING = {
  'version': 1,
  'disable_existing_loggers': True,
  'root': {
    'level': 'WARNING',
    'handlers': ['sentry']},
  'formatters': {
    'verbose': {
      'format': ("%(levelname)s %(asctime)s %(module)s %(process)d "
                 "%(thread)d %(message)s")}},
  'handlers': {
    'sentry': {
      'level': 'ERROR',
      'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler'},
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
      'formatter': 'verbose'}},
  'loggers': {
    'django.db.backends': {
      'level': 'ERROR',
      'handlers': ['console'],
      'propagate': False},
    'raven': {
      'level': 'DEBUG',
      'handlers': ['console'],
      'propagate': False},
    'sentry.errors': {
      'level': 'DEBUG',
      'handlers': ['console'],
      'propagate': False}}}
