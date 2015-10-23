#!/usr/bin/env python
"""
Is the 'main' file and is used for execute the aplication.
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.busineme")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
