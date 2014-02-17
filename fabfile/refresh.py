from fabric.api import *
from fabric.contrib.project import rsync_project
from fabric.colors import *


@task
@roles('app')
def db():
    date_format_str = run('date +\%Y\%m\%d')
    filename = '%s.%s.sql.bz2' % (env.application, date_format_str)
    local('dropdb --if-exists %s' % env.database)
    local('createdb %s' % env.database)
    get('%s/sql/%s' % (env.remote_backups_dir, filename), '.')
    local('bzcat %s | psql %s > /dev/null' % (filename, env.database))
    local('rm %s' % filename)


@task
@roles('app')
def media():
    rsync_project(
        remote_dir='%s/media/' % env.remote_backups_dir,
        local_dir='media',
        delete=True,
        upload=False,
        default_opts='-vauz')


@task
def search():
    local('python manage.py rebuild_index --noinput')


@task(default=True)
def all():
    execute(db)
    execute(media)
