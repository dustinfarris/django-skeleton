#!/usr/bin/env python
from os import environ
import sys


if __name__ == "__main__":
    if 'test' in sys.argv:
        environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.test")
    else:
        environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "{{ project_name}}.settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
