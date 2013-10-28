from fabric.api import *


@task(default=True)
def merge():
    current_branch = local('git branch | grep "*"', capture=True)[2:]
    if current_branch == env.staging_branch:
        abort('You are already on the %s branch!' % env.staging_branch)
    msg = "Merge branch '%s' into %s" % (current_branch, env.staging_branch)
    local('git fetch --prune origin')
    local('git checkout %s' % env.staging_branch)
    local('git pull')
    local('git merge --no-ff --no-edit --commit -m "%s" %s' % (msg, current_branch))
    local('git push origin %s' % env.staging_branch)
    local('git checkout %s' % current_branch)
