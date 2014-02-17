import random

from fabric.api import *


default_settings = """from .server import *

DEBUG = False
TEMPLATE_DEBUG = False
SECRET_KEY = '{secret_key}'
ALLOWED_HOSTS = ['{hostname}']

URL_PREFIX = '{hostname}'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
CELERY_ALWAYS_EAGER = False

DATABASES['default']['HOST'] = '{db_host}'
CELERY_RESULT_BACKEND = 'redis://{db_host}'
"""


@roles('app')
def init_db():
    run('createdb %s' % env.database)


@roles('app')
def init_app():
    run('mkdir -p %s' % env.remote_sites_dir)
    run('mkdir -p %s' % env.remote_settings_dir)
    run('mkdir -p %s' % env.remote_media_dir)
    run('mkdir -p %s' % env.remote_scripts_dir)
    secret_key = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    run('echo "%s" > %s' % (
        default_settings.format(
            application=env.application,
            secret_key=secret_key,
            hostname=env.hostname,
            db_host=env.db_host),
        env.remote_settings_path))
    run('echo "#!/bin/sh" > %s/%s.sh' % (env.remote_scripts_dir, env.application))
    execute('deploy.full', initdb=True, with_restart=False)
    server_configuration = (
        'ln -sfn {base}/config/nginx/{hostname}.conf /etc/nginx/sites-available/.',
        'ln -sfn /etc/nginx/sites-available/{hostname}.conf /etc/nginx/sites-enabled/.',
    )
    for command in server_configuration:
        sudo(
            command.format(
                app=env.application,
                base=env.remote_location,
                hostname=env.hostname),
            shell=False,
            pty=False)
    execute('restart')


@task
def init():
    execute(init_db)
    execute(init_app)


@task
@roles('app')
def quick(with_restart=True):
    with cd(env.remote_location):
        git_branch = run('git branch')
        if '* %s' % env.branch not in git_branch:
            abort('The server is not on the %s branch' % env.branch)
        git_status = run('git status')
        if 'Changes to be committed' in git_status:
            abort('There are uncommitted changes on the server.')

        run('git pull')

        with prefix('source env/bin/activate'):
            run('make update')
    if with_restart is True:
        execute('restart')


@task(default=True)
@roles('app')
def full(initdb=False, with_restart=True):
    with cd(env.remote_sites_dir):
        old_instances = run('ls | grep "%s_" || true' % env.application).splitlines()

    system_now = run('date +\%Y\%m\%d\%H\%M\%S')
    deploy_path = '%s/%s_%s' % (env.remote_sites_dir, env.application, system_now)

    run('git clone -q %s %s' % (env.repo_url, deploy_path))

    with cd(deploy_path):
        run('git checkout %s' % env.branch)
        run('ln -sf %s media' % env.remote_media_dir)
        run('ln -sf %s %s/%s' % (env.remote_settings_path, deploy_path, env.relative_settings_path))
        run('virtualenv env')

        with prefix('source env/bin/activate'):
            with shell_env(LANG='en_US.UTF-8'):
                run('make install')
            if initdb is True:
                run('make initdb')
            run('make update')

    run('ln -sfn %s %s' % (deploy_path, env.remote_location))
    run('source %s/%s.sh' % (env.remote_scripts_dir, env.application))

    for instance in old_instances:
        run('rm -rf %s/%s' % (env.remote_sites_dir, instance))

    if with_restart is True:
        execute('restart')
