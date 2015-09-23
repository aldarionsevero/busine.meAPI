"""
Busine-me API
Universidade de Brasilia - FGA
Tecnicas de Programação, 2/2015
@file models.py
Models for User an Rank.
"""
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate
from django.db import models
from django.http import HttpResponse
import logging

logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s',
                    filename='authentication/logging/modelsLogging.log',
                    level=logging.DEBUG)


class RankPosition(models.Model):

    """Model that carries the user rank based in description and points."""

    description = models.CharField(max_length=100)
    min_points = models.IntegerField()
    serialize_fields = ['description',
                        'min_points']

    def __str__(self):
        return "{} - {}".format(self.id, self.description)


class BusinemeUser(AbstractUser):

    """Model for User. Inherits AbstractUser and overrides specific things."""

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
        """Saves user."""
        self.username = self.username.lower()
        super(BusinemeUser, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} {}".format(self.id, self.username, self.email)

    def create_user(self, request):
        """
        PUT method for create an user by receiving
        four arguments from application, using POST method for security.
        """
        self.username = request.POST['username']
        self.first_name = request.POST['first_name']
        self.last_name = request.POST['last_name']
        self.set_password(request.POST['password'])

        username = self.username
        first_name = self.first_name
        email = self.email

        assert self is None
        assert username is None
        assert first_name is None
        assert email is None

        assert username == ''
        assert first_name == ''
        assert email == ''

        logging.debug(
            'Object %s - username %s - first_name %s - email - %s',
            self, username, first_name, email)

        self.save()

    def update_user_first_last_name(self, request):
        """
        Define method for update first_name and last_name given a
        specific BuslineUser using the POST method for security.
        """
        self.first_name = request.POST['first_name']
        self.last_name = request.POST['last_name']

        username = self.username
        first_name = self.first_name
        email = self.email

        assert self is None
        assert username is None
        assert first_name is None
        assert email is None

        assert username == ''
        assert first_name == ''
        assert email == ''

        logging.debug(
            'Object %s - username %s - first_name %s - email - %s',
            self, username, first_name, email)

        self.save()

    def update_user_password(self, request):

        update_user = request.user

        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        assert new_password is None
        assert confirm_new_password is None

        assert new_password == ''
        assert confirm_new_password == ''

        logging.debug(
            'Object %s - password could not be changed. Something came Null ',
            self, new_password, confirm_new_password)

        if new_password.isEquals(confirm_new_password):
            update_user.set_password(new_password)
            update_user.save()

            message_log_sucess = "Changes saved"
            response = HttpResponse(message_log_sucess)
        else:
            message_log_fail = "Unable to change password \
                                password's don't match"
            response = HttpResponse(message_log_fail)

        return response

    def user_authenticate(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        return user
