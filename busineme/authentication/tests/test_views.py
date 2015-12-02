"""
Busine-me API
Universidade de Brasilia - FGA
Tecnicas de Programacao, 2/2015
@file models.py
Testing models authentication.
"""
from django.test import TestCase
from django.test import Client
from ..models import RankPosition
from ..models import BusinemeUser

"""
This class is used for create tests some validations in RankPosition.
"""


class TestLoginView(TestCase):

    """
    This test method is used for make the tests in changes on the view login.
    """

    def setUp(self):
        self.client = Client()

    """
    This test method is used for analysis of method obtain user is taking place
    in the correct way.
    """

    def test_get(self):
        response = self.client.get('/auth/users/')
        self.assertEquals(response.status_code, 200)

    """
    This test method is used for analysis of if the method is behaving in the
    correct way.
    """

    def test_get_user(self):
        user = BusinemeUser()
        user.name = "test-user"
        user.username = "test-user"
        user.email = "user-test@email.com"
        rank = RankPosition()
        rank.description = " "
        rank.min_points = 0
        rank.max_points = 99
        rank.save()
        user.rank = rank
        user.save()
        user = BusinemeUser.objects.get(username="test-user")
        response = self.client.get('/auth/users/' + str(user.id) + '/')
        self.assertEquals(response.status_code, 200)

    """
    This test method is used for analysis if the save user is registered in the
    database.
    """

    def test_get_user_not_found(self):
        response = self.client.get('/auth/users/10000/')
        self.assertEquals(response.status_code, 200)
