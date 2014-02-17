#!/usr/bin/env python3
from os import environ
import sys


if __name__ == "__main__":
    environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
