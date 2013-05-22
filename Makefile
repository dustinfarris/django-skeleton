add-submodules:
	git submodule add https://github.com/jlong/sass-twitter-bootstrap.git {{ project_name }}/static/stylesheets/bootstrap
	git submodule init

update-submodules:
	git submodule init
	git submodule update

develop: update-submodules
	npm install
	pip install "flake8>=1.7" --use-mirrors
	pip install --upgrade -r requirements/development.txt --use-mirrors
	pip install --upgrade -r requirements/test.txt --use-mirrors
	pip install --upgrade -r requirements/core.txt --use-mirrors
	easy_install readline
	echo "from {{ project_name }}.settings.development import *" > src/{{ project_name }}/settings/__init__.py

test: lint test-coffee test-python test-behave

test-python: test-models test-unit test-integration

test-models:
	@echo "Running Django model tests"
	python manage.py test tests/models --logging-filter=-south || exit 1
	@echo ""

test-unit:
	@echo "Running Python unit tests"
	python manage.py test tests/unit --with-doctest --doctest-options=+ELLIPSIS --logging-filter=-south || exit 1
	@echo ""

test-integration:
	@echo "Running Python integration tests"
	python manage.py test tests/integration --logging-filter=-south || exit 1
	@echo ""

test-behave:
	@echo "Running Functional behavior tests"
	behave tests/functional
	@echo ""

test-wip:
	@echo "Runing Functional behavior tests for 'works in progress'"
	behave -w tests/functional
	@echo ""

test-coverage:
	@echo "Running model, unit, and integration tests with coverage enabled"
	python manage.py test --with-doctest --doctest-options=+ELLIPSIS --with-coverage --cover-erase --cover-package=industrymaps,maps,accounts,src --cover-html tests src
	open cover/index.html
	@echo ""

lint: lint-python

lint-python:
	@echo "Linting Python files"
	flake8 --ignore=E121,W404,F403 --exclude=./env/*,./venv/*,migrations,.git,./tests/functional/features,./tests/functional/steps . || exit 1
	@echo ""
