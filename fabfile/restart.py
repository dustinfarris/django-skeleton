from fabric.api import *


@task
@roles('app')
def apache():
    sudo('service apache2 restart', shell=False, pty=False)


@task
@roles('app')
def nginx():
    sudo('service nginx restart', shell=False, pty=False)


@task
@roles('app')
def memcached():
    sudo('service memcached restart', shell=False, pty=False)


@task
@roles('app')
def celery():
    sudo('service celeryd restart', shell=False, pty=False)
    sudo('service celerybeat restart', shell=False, pty=False)


@task(default=True)
def all():
    execute(apache)
    execute(nginx)
    execute(celery)
    execute(memcached)
