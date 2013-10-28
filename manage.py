#!/usr/bin/env python3
from os import environ
from os.path import abspath, dirname, join
import sys


if __name__ == "__main__":
    source_dir = abspath(join(dirname(__file__), 'app'))
    if source_dir not in sys.path:
        sys.path.insert(0, source_dir)
    environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
