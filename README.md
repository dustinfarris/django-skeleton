# {{ project_name }}

A very basic Django skeleton project.


## Development

### Prerequisites

You will need [homebrew][] and the following:

* Python (>=3.3 preferred)
* Memcached
* PostgreSQL
* Redis (for Celery results)
* virutalenvwrapper
* Django

```console
brew update && brew upgrade
brew install python3 postgresql memcached
createuser -s web
pip3 install --upgrade Django virtualenvwrapper
```

To make virtualenvwrapper use your homebrewed Python, add the following to your
`~/.bash_profile`:

```bash
export VIRTUALENVWRAPPER_PYTHON="/usr/local/bin/python3"
source "/usr/local/bin/virtualenvwrapper.sh"
```

And here's a handy alias to drop into your `~/.profile` or `~/.bashrc`,
whichever you prefer:

```bash
alias mkenv='mkvirtualenv `basename $PWD` && setvirtualenvproject'
```

### Creating a new project

Create a new Django project using the django-skeleton template:

```console
django-admin.py startproject \
--template=https://github.com/dustinfarris/django-skeleton/archive/master.zip \
--extension=py,md \
--name=Makefile,.gitignore,.coveragerc \
myproject
```

Perform an initial commit:

```console
cd myproject
git init
git add -A
git commit -m "Initial commit"
```

Set up your environment (using the alias from earlier):

```console
mkenv
make develop
```

All tests should pass:

```console
make test
```

Create and sync your database:

```console
createdb myproject
make initdb
```

Run the Django server to start development:

```console
python manage.py runserver 0.0.0.0:8000
```

And you're off to the races!


[homebrew]: http://brew.sh/
