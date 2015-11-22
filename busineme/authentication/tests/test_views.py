from django.test import TestCase
from django.test import Client 
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from ..models import RankPosition
from ..models import BusinemeUser

"""
This class is used for create tests some validations in RankPosition.
"""


class TestLoginView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get(self):
        response = self.client.get('/auth/users/')
        self.assertEquals(response.status_code, 200)
    
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
        print (user.id)
        user = BusinemeUser.objects.get(username="test-user")
        print (user.id)
        response = self.client.get('/auth/users/'+str(user.id)+'/')
        self.assertEquals(response.status_code, 200)


