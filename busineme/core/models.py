"""
Busine-me API
Universidade de Brasilia - FGA
Técnicas de Programação, 2/2015
@file models.py
Busline Company and Terminal models.
"""
from django.db import models


class Busline(models.Model):

    """Busline Model."""

    line_number = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=255)
    via = models.CharField(max_length=255)
    route_size = models.FloatField()  # unit: kilometers
    fee = models.DecimalField(decimal_places=2, max_digits=4)  # unit: BRL (R$)
    company = models.ForeignKey('Company', null=True)
    terminals = models.ManyToManyField('Terminal')

    serialize_fields = ['line_number',
                        'description',
                        'via',
                        'route_size',
                        'fee',
                        'company',
                        'terminals']

    def __str__(self):
        return "{} - {}".format(self.line_number, self.description)

    @classmethod
    def api_filter_startswith(cls, line_number):
        r"""
        If API is up, send requisition and returns buslines with the \
        specified line number. If API is down, searches local database to\
        return buslines with the specified line number.
        """
        objects = cls.objects.filter(line_number__startswith=line_number)
        return objects


class Company(models.Model):

    """Company Model."""

    name = models.CharField(max_length=255)

    serialize_fields = ['name']

    def __str__(self):
        return "{}".format(self.name)


class Terminal(models.Model):

    """Terminal Model."""

    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)

    serialize_fields = ['description',
                        'address']

    def __str__(self):
        return "{}".format(self.description)
