"""
Busine-me API
Universidade de Brasilia - FGA
Tecnicas de Programacao, 2/2015
@file models.py
Testing models authentication.
"""
from django.test import TestCase
from django.db import IntegrityError
from ..models import RankPosition, BusinemeUser

"""
This class is used for create tests some validations in RankPosition.
"""


class TestRankPosition(TestCase):

    def setUp(self):
        self.rank = RankPosition()

    def test_str(self):
        self.rank.id = 1
        self.rank.description = "Rank A"
        self.rank.min_points = 10
        self.assertEquals("1 - Rank A", self.rank.__str__())

    """
    This test method is used for analysis if the fields of the forms so that
    are not empty.
    """

    def test_empty_fields(self):
        self.assertRaises(IntegrityError, self.rank.save)

    def test_empty_min_points_field(self):
        self.rank.description = "Rank A"
        self.assertRaises(IntegrityError, self.rank.save)

    """
    This test method is used for analysis if the save ranking method is
    behaving in the correct way.
    """

    def test_save(self):
        self.rank.id = 1
        self.rank.description = "Rank A"
        self.rank.min_points = 0
        self.rank.save()

        self.assertEquals(1, len(RankPosition.objects.all()))

"""
This class is used for create tests some validation in BusinemeUser.
"""


class TestBusinemeUser(TestCase):

    """
    This test method is used for make the tests in changes on the user.
    """

    def setUp(self):
        self.user = BusinemeUser()
        self.rank = RankPosition()
        self.rank.description = "Rank A"
        self.rank.min_points = 0
        self.rank.save()

        self.user.id = 1
        self.user.username = "Username"
        self.user.email = "email@email.com"
        self.user.first_name = "First"
        self.user.rank = self.rank

    def test_str(self):
        self.assertEquals("1 - Username email@email.com", self.user.__str__())

    """
    This test method is used for analysis if the save user is behaving in the
    correct way.
    """

    def test_save(self):
        self.user.save()
        self.assertEquals("username", self.user.username)
