# {{ project_name }}

Very basic Django skeleton project.

## Prerequisites

You will need [homebrew][] to install these:

```console
brew update && brew upgrade
brew install postgresql
createuser -s web
brew install memcached
brew install python3
pip3 install --upgrade virtualenvwrapper
pip3 install --upgrade Django
```

If installing virtualenvwrapper for the first time, you will need to add the following to `~/.bash_profile`:

```bash
export VIRTUALENVWRAPPER_PYTHON="/usr/local/bin/python3"
source "/usr/local/bin/virtualenvwrapper.sh"
```

And here's a handy alias to drop into `~/.profile` or `~/.bashrc` (whichever you use):

```bash
alias mkenv='mkvirtualenv `basename $PWD` && setvirtualenvproject && add2virtualenv app'
```

## Creating a new project

Create a new Django project using this template:

```console
django-admin.py startproject --template=https://github.com/dustinfarris/django-skeleton/zipball/master --extension=py,md --name=Makefile,.gitignore,circle.yml,package.json <projectname>
```

Initial commit:

```console
cd <projectname>
git init
git add -A
git commit -m "Initial commit"
```

Set up your environment (using the alias from earlier):

```console
mkenv
make install
```

Add your repo information to fabfile (for automatic deploys, refreshes, etc..):

```console
vi fabfile/__init__.py
```

All tests should pass:

```console
make
```

Create and sync your database:

```console
createdb <projectname>
python manage.py syncdb --all
python manage.py migrate --fake
python manage.py runserver 0.0.0.0:8000
```

Done!


[homebrew]: http://brew.sh
