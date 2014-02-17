"""
{{ project_name }}
==================

Description goes here.

:copyright: (c) 2014 by Author
"""
from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


setup_requires = []
if 'test' in sys.argv:
    setup_requires.append('pytest')

dev_requires = [
    'flake8',
    'ipdb',
]

tests_require = [
    'pytest-cov',
    'pytest-django',
    'factory_boy',
]

install_requires = [
    'Django==1.6.2',
    'Pillow==2.3.0',
    'psycopg2==2.5.2',
    'South==0.8.4',
    'celery[redis]==3.1.8',
    'raven==4.0.4',
    'gunicorn==18.0',
    'python3-memcached==1.51',
]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='{{ project_name }}',
    version='0.0-dev',
    packages=['{{ project_name }}'],
    install_requires=install_requires,
    extras_require={
        'tests': tests_require,
        'dev': dev_requires,
    },
    tests_require=tests_require,
    cmdclass={'test': PyTest},
)
