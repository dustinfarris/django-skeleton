import sys

from core import *


DEBUG = True

# Disable the use of South migrations while testing
SOUTH_TESTS_MIGRATE = False

# Use sqlite and speedy password hashing for testing
if 'test' in sys.argv:
  DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}
  PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)

# Turn on debug-level logging for applications
for application in []:
  LOGGING['loggers'].update({
    application: {
      'level': 'DEBUG',
      'handlers': ['console'],
      'propagate': False,
    }
  })
  
# Disable Raven logging (make test running less noisy)
del(LOGGING['loggers']['raven'])

INTERNAL_IPS += (
  '127.0.0.1',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Uncomment the following to test django_compressor's output in development
# COMPRESS_ENABLED = True

# This effectively disables any server side caching in development
CACHES['default']['BACKEND'] = 'django.core.cache.backends.dummy.DummyCache'

INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

DEBUG_TOOLBAR_PANELS = (
  'debug_toolbar.panels.version.VersionDebugPanel',
  'debug_toolbar.panels.timer.TimerDebugPanel',
  'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
  'debug_toolbar.panels.headers.HeaderDebugPanel',
  'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
  'debug_toolbar.panels.template.TemplateDebugPanel',
  'debug_toolbar.panels.sql.SQLDebugPanel',
  'debug_toolbar.panels.signals.SignalDebugPanel',
  'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
  'INTERCEPT_REDIRECTS': False,
  # 'SHOW_TOOLBAR_CALLBACK': None,
  # 'EXTRA_SIGNALS': [],
  'HIDE_DJANGO_SQL': True,
  # 'TAG': 'body',
  'ENABLE_STACKTRACES': False,
}

# Uncomment the following to enable devserver, see default settings below
# INSTALLED_APPS += ('devserver',)

DEVSERVER_IGNORED_PREFIXES = ['/media', '/static', '/favicon.ico']
DEVSERVER_DEFAULT_ADDR = '0.0.0.0'
DEVSERVER_TRUNCATE_SQL = True
DEVSERVER_SQL_MIN_DURATION = 1 # time in ms
DEVSERVER_AUTO_PROFILE = False

DEVSERVER_MODULES = (
  # 'devserver.modules.sql.SQLRealTimeModule',
  'devserver.modules.sql.SQLSummaryModule',
  'devserver.modules.profile.ProfileSummaryModule',

  # Modules not enabled by default
  # 'devserver.modules.ajax.AjaxDumpModule',
  'devserver.modules.profile.MemoryUseModule',
  # 'devserver.modules.cache.CacheSummaryModule',
  # 'devserver.modules.profile.LineProfilerModule',
)
