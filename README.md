# {{ project_name }}

## Technologies

The following languages are used throughout this project:
* Jade (HTML)
* SASS (CSS)
* Python
* jQuery (JavaScript)
* Markdown

## Prerequisites

By default, this Django project requires:
* Python >= 2.7
* PostgreSQL >= 9.1
* memcached
* Markdown

## Local development

After git-clone'ing the project, set up a database and a web superuser:

	createuser -s web
	createdb {{ project_name }}

Set up your virtualenv:

	virtualenv env
	source env/bin/activate
	pip install -r requirements-dev.txt

Create the file ```{{ project_name }}/settings/__init__.py```:

    from development import *
    
Set the executable flag on manage.py:

  chmod 744 manage.py
	
Sync the database:

	./manage.py syncdb --all
	./manage.py migrate --fake
	
Gather static media:
	
	./manage.py collectstatic
	
Run the development server:
	
	./manage.py runserver 0.0.0.0:8000
