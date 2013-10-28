from fabric.api import *


@task(default=True)
def new(name=None):
    if name is None:
        name = prompt('Name:')
    local('git checkout %s' % env.production_branch)
    local('git pull origin %s' % env.production_branch)
    local('git checkout -b %s' % name)
    local('git push -u origin %s' % name)
