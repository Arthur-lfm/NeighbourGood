#!/usr/bin/env python
import os
import sys

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'pollme.settings_dev':
    settings_module = 'pollme.settings_dev'
else:
    settings_module = 'pollme.settings_test'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pollme.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
