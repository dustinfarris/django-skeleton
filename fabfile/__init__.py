from fabric.api import env, task

from fabfile import deploy, refresh, restart, stage, sync, topic


__all__ = ['deploy', 'refresh', 'restart', 'stage', 'sync', 'topic', 'production', 'staging']


# ENVIRONMENT

env.application = '{{ project_name }}'
env.repo_url = 'git@github.com:myuser/{{ project_name }}.git'
env.production_branch = 'master'
env.staging_branch = 'staging'


# SERVER CONFIGURATION

@task
def staging():
    env.hostname = 'staging.api.{{ project_name }}.com'
    env.branch = env.staging_branch
    env.roledefs = {
        'app': ['web@192.111.11.11'],
        'db': ['web@192.111.11.11'],
    }


@task
def production():
    env.hostname = 'api.{{ project_name }}.com'
    env.branch = env.production_branch
    env.roledefs = {
        'app': ['web@192.222.22.22'],
        'db': ['web@192.222.22.22'],
    }


env.remote_home_dir = '/var/www'
env.remote_location = '%s/%s' % (env.remote_home_dir, env.application)
env.remote_sites_dir = '%s/_sites' % env.remote_home_dir
env.remote_settings_dir = '%s/_settings' % env.remote_home_dir
env.remote_media_dir = '%s/_media/%s' % (env.remote_home_dir, env.application)
env.remote_scripts_dir = '%s/_scripts' % env.remote_home_dir
env.remote_backups_dir = '/var/backups/%s' % env.application
env.remote_settings_path = "%s/%s.py" % (env.remote_settings_dir, env.application)
env.relative_settings_path = 'app/%s/settings/__init__.py' % env.application


# DATABASE

env.database = env.application


# MISCELLANEOUS SETTINGS

env.colorize_errors = True
