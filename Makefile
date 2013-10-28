test: lint test-python

lint:
	@echo "Linting Python files"
	flake8 --ignore=E121,W404,F403,E501 --exclude=./env/*,./venv/*,migrations,.git . || exit 1
	@echo ""

test-python: test-unit test-integration

test-unit:
	@echo "Running Python unit tests"
	python manage.py test --settings={{ project_name }}.settings.test tests.unit
	@echo ""

test-integration:
	@echo "Running Python integration tests"
	python manage.py test --settings={{ project_name }}.settings.test tests.integration
	@echo ""
	
initdb:
	python manage.py syncdb --all --noinput
	python manage.py migrate --fake

update-submodules:
	git submodule init
	git submodule update

update: update-submodules
	python manage.py migrate
	python manage.py collectstatic --noinput

install-core:
	pip install --upgrade --use-mirrors setuptools
	easy_install -U Pillow
	pip install --upgrade --use-mirrors -r requirements/core.txt

install-development:
	pip install --upgrade --use-mirrors -r requirements/development.txt

install-test:
	pip install --upgrade --use-mirrors flake8
	pip install --upgrade --use-mirrors -r requirements/test.txt

install: install-core install-development install-test
	echo "from {{ project_name }}.settings.development import *" > app/{{ project_name }}/settings/__init__.py

