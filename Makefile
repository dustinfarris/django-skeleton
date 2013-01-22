develop: add-submodules update-submodules
	pip install "flake8>=1.7" --use-mirrors
	pip install --upgrade -r requirements-development.txt --use-mirrors
	pip install --upgrade -r requirements-test.txt --use-mirrors
	pip install --upgrade -r requirements.txt --use-mirrors
	easy_install readline
	echo "from development import *" > {{ project_name }}/settings/__init__.py

add-submodules:
	git submodule add https://github.com/dustinfarris/fabfile.git

update-submodules:
	git submodule init
	git submodule update

test: lint test-python

test-python:
	@echo "Running Python tests"
	python manage.py test --logging-filter=-south || exit 1
	@echo ""

lint: lint-python

lint-python:
	@echo "Linting Python files"
	flake8 --ignore=E111,E121,W404 --exclude=./env/*,./venv/*,migrations,.git . || exit 1
	@echo ""
