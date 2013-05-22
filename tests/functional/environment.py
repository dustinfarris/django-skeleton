from os import environ
from os.path import join
import subprocess


environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.selenium")


from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from django.core.management import call_command
from django.db import connections
from django.test.testcases import LiveServerThread
from django.test.utils import setup_test_environment, teardown_test_environment
from selenium import webdriver


def _reset_db():
    call_command('flush', interactive=False, verbosity=False)
    call_command('loaddata', 'all', verbosity=False)
    user = User.objects.create(
        username="bob@bob.com",
        email="bob@bob.com",
        is_staff=False,
        is_superuser=False)
    user.set_password("bob")
    user.save()
    superuser = User.objects.create(
        username="admin",
        email="admin@localhost",
        is_staff=True,
        is_superuser=True)
    superuser.set_password("admin")
    superuser.save()


def before_all(context):
    call_command('syncdb', interactive=False, verbosity=False)
    call_command('flush', interactive=False, verbosity=False)
    call_command('migrate', interactive=False, verbosity=False)
    call_command('collectstatic', interactive=False, verbosity=False)
    _reset_db()
    setup_test_environment()
    setattr(settings, "LINKEDIN_REDIRECT_DOMAIN", "localhost:8081")

    # Taken from Django's LiveServerTestCase
    connections_override = {}
    for conn in connections.all():
        # If using in-memory sqlite databases, pass the connections to
        # the server thread.
        if (conn.settings_dict['ENGINE'] == 'django.db.backends.sqlite3'
                and conn.settings_dict['NAME'] == ':memory:'):
            # Explicitly enable thread-shareability for this connection
            conn.allow_thread_sharing = True
            connections_override[conn.alias] = conn
    # Launch the server's thread
    specified_address = environ.get(
        'DJANGO_LIVE_TEST_SERVER_ADDRESS', 'localhost:8081')
    possible_ports = []
    try:
        host, port_ranges = specified_address.split(':')
        for port_range in port_ranges.split(','):
            extremes = map(int, port_range.split('-'))
            assert len(extremes) in [1, 2]
            if len(extremes) == 1:
                possible_ports.append(extremes[0])
            else:
                for port in range(extremes[0], extremes[1] + 1):
                    possible_ports.append(port)
    except Exception:
        raise ImproperlyConfigured(
            'Invalid address("%s") for live server.' % specified_address)
    context.server_thread = LiveServerThread(
        host, possible_ports, connections_override)
    context.server_thread.daemon = True
    context.server_thread.start()

    # Wait for the live server to be ready
    context.server_thread.is_ready.wait()
    if context.server_thread.error:
        raise context.server_thread.error

    context.browser = webdriver.Firefox()
    context.browser.implicitly_wait(2)
    context.url = lambda u: 'http://%s:%s%s' % (
        context.server_thread.host, context.server_thread.port, u)


def after_all(context):
    # Redirecting to another page helps prevent a Django error when closing
    # the liveserver thread
    context.browser.get(context.url('/'))
    context.browser.quit()
    if hasattr(context, 'server_thread'):
        context.server_thread.join()
    teardown_test_environment()
    subprocess.call(['rm', '-rf', join(settings.PROJECT_DIR, '..', 'static')])


def after_scenario(context, scenario):
    _reset_db()
