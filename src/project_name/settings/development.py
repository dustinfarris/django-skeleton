from {{ project_name }}.settings.settings import *


DEBUG = True
TEMPLATE_DEBUG = True

# Turn on debug-level logging for applications (add yours to the list)
for application in []:
    LOGGING['loggers'].update({
        application: {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False}})

# Disable Raven logging (make test running less noisy)
del(LOGGING['loggers']['raven'])

INTERNAL_IPS += (
    '127.0.0.1',)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Uncomment the following to test django_compressor's output in development
# COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False

# This effectively disables any server side caching in development
CACHES['default']['BACKEND'] = 'django.core.cache.backends.dummy.DummyCache'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

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
    'debug_toolbar.panels.logger.LoggingPanel',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    # 'SHOW_TOOLBAR_CALLBACK': None,
    # 'EXTRA_SIGNALS': [],
    'HIDE_DJANGO_SQL': True,
    # 'TAG': 'body',
    'ENABLE_STACKTRACES': False}

INSTALLED_APPS += ('django_extensions',)