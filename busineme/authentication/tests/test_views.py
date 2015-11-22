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
