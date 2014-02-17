develop: install
	pip install -q "file://`pwd`#egg={{ project_name }}[dev]"
	pip install -q "file://`pwd`#egg={{ project_name }}[tests]"
	echo "from .server import *" > {{ project_name }}/settings/__init__.py

install:
	pip install -q -e .

initdb:
	python manage.py syncdb --all --noinput
	python manage.py migrate --fake

update:
	python manage.py migrate
	python manage.py collectstatic -v0 --noinput

test: develop lint test-python

lint:
	@echo "Linting Python files"
	flake8 {{ project_name }}
	@echo ""

test-python:
	@echo "Running Python tests"
	python setup.py -q test || exit 1
	@echo ""

coverage: develop
	py.test --cov={{ project_name }} --cov-report=html
	open htmlcov/index.html
