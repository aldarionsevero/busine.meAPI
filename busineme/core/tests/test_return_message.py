"""
Busine-me API
Universidade de Brasilia - FGA
Tecnicas de Programacao, 2/2015
@file return_message.py
Testing return messages in core.
"""

from django.test import TestCase
from core.return_message import ReturnMessage

STATUS_CODE_OK = 200
STATUS_CODE_CREATED = 201
STATUS_CODE_NOT_FOUND = 404
STATUS_CODE_SERVER_ERROR = 500
STATUS_UNDEFINED = 100000


class TestReturnMessage(TestCase):

    def setUp(self):
        self.response_message = ReturnMessage()

    def test_return_for_200(self):
        message = self.response_message.return_message(
            STATUS_CODE_OK)
        self.assertEquals(message['return_message'], 'Everything Worked.')

    def test_return_for_201(self):
        message = self.response_message.return_message(
            STATUS_CODE_CREATED)
        self.assertEquals(message['return_message'], 'Successfully Created.')
