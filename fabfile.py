from fabric.api import abort, cd, env, execute, hosts, local, prefix, prompt, run, settings, sudo
from fabric.contrib import django
from fabric.contrib.console import confirm


PROJECT = '{{ project_name }}'
DATABASE = '{{ project_name }}'
REBUILD_INDEX = False
django.settings_module('{{ project_name }}.settings')
env.use_ssh_config = True


def _validate_path(path):
  path = path.strip()
  paths = ('staging', 'production')
  if path in paths:
    return path
  else:
    raise ValueError("Choose from: " + " or ".join(paths))


def refresh():
  """Update local database and copy asset uploads from backups on jhot."""
  path = prompt(
      "Which database should be operated on (staging or production)?", 
      default='production', 
      validate=_validate_path)
  refresh_db(path, DATABASE, PROJECT)
  copy_media(path, PROJECT)
  if REBUILD_INDEX:
    rebuild_index()


def refresh_db(path, db_name, proj_name):
  """Update local database with appropriate backup on jhot."""
  drop_db(db_name)
  create_db(db_name)
  copy_db(path, proj_name, db_name)
  load_db(db_name)
  
  
def drop_db(db_name):
  """Drop local database."""
  if confirm("Are you sure you want to delete your %s database?" % db_name):
    with settings(warn_only=True):
      result = local("dropdb %s" % db_name)
      if result.failed:
        # Don't abort() so refresh()/refresh_db() can continue with create_db()
        print("dropdb skipped as database doesn't exist")
  else:
    abort("dropdb cancelled")


def create_db(db_name):
  """Create local database"""
  local("createdb %s -T template_postgis" % db_name)


def copy_db(path, proj_name, db_name):
  """
  scp's the latest SQL backup from staging.
  """
  local("scp backups@jhot:/var/backups/%s/%s/sql/%s.sql.gz ." % (proj_name, path, db_name + ".`date +\%Y\%m\%d`"))


def load_db(db_name):
  local("gunzip %s.sql.gz" % (db_name + ".`date +\%Y\%m\%d`"))
  local("psql %s < %s.sql > /dev/null 2> /dev/null" % (db_name, db_name + ".`date +\%Y\%m\%d`"))
  # Remove the SQL dump so this is not accidentally committed.
  local("rm %s.sql*" % (db_name + ".`date +\%Y\%m\%d`"))


def copy_media(path, proj_name):
  """Copy asset uploads from jhot."""
  local("rsync -vauz --delete backups@jhot:/var/backups/%s/%s/media/ media" % (proj_name, path))


def rebuild_index():
  """Rebuild the local search index."""
  local("./manage.py rebuild_index  --noinput")


def update_staging():
  execute(update_staging_code)
  execute(restart_staging_servers)


@hosts('web@jhot')
def update_staging_code(proj_name):
  with cd('/home/web/%s' % proj_name):
    result = run('git branch')
    if "* master" not in result:
      abort("The staging server is not on the master branch.")
    result = run('git status')
    if 'Changes to be committed' in result:
      abort("There are uncommitted changes on the staging server. Please ask a developer to fix this and to never edit on the staging server again.")
    run('git pull')
    with prefix('source /home/web/%s/env/bin/activate' % proj_name):
      run('./manage.py migrate')
      run('./manage.py rebuild_index --noinput')
      run('./manage.py collectstatic --noinput')


@hosts('jhot')
def restart_staging_servers():
  sudo("/etc/init.d/apache2 restart")
  sudo("/etc/init.d/memcached restart")
  sudo("/etc/init.d/nginx restart")