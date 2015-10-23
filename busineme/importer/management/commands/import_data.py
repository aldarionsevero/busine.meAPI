# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from importer.parser import Parser

"""
This class is used for populate the database.
"""


class Command(BaseCommand):

    """
    This method is used for create objects based in parser.
    """

    def handle(self, *args, **options):
        parser = Parser()
        parser.import_data()
