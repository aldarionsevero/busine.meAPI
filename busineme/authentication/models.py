"""
Busine-me API
Universidade de Brasilia - FGA
Tecnicas de Programacao, 2/2015
@file models.py
Models for User an Rank.
"""
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate
from django.db import models
from django.http import HttpResponse
import logging


FORMAT = '%(levelname)s: %(asctime)s %(message)s'
logging.basicConfig(format=FORMAT,
                    filename='authentication/logging/modelsLogging.log',
                    level=logging.DEBUG)


class RankPosition(models.Model):

    """
    Model that carries the user rank based in description and points.
    """

    description = models.CharField(max_length=100)
    min_points = models.IntegerField()
    serialize_fields = ['description',
                        'min_points']

    def __str__(self):
        return "{} - {}".format(self.id, self.description)


class BusinemeUser(AbstractUser):

    """
    Model for User. Inherits AbstractUser and overrides specific things.
    """

    pontuation = models.IntegerField(default=0)
    rank = models.ForeignKey(RankPosition, null=True)

    serialize_fields = ['username',
                        'first_name',
                        'last_name',
                        'rank',
                        'pontuation',
                        'email',
                        'id',
                        'date_joined']

    def save(self, *args, **kwargs):
        """
        Saves user.
        """
        self.username = self.username.lower()
        super(BusinemeUser, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} {}".format(self.id, self.username, self.email)


