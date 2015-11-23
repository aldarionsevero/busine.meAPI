"""
Busine-me API
Universidade de Brasilia - FGA
Tecnicas de Programacao, 2/2015
@file views.py
Views (on classic MVC, controllers) with methods that control the requisitions
for the user authentication and manipulation.
"""
from django.views.generic import View
from core.serializers import serialize_objects
from core.serializers import serialize
from .models import BusinemeUser
from django.http import JsonResponse
from core.return_message import return_message
import logging

STATUS_OK = 200
STATUS_NOT_FOUND = 404
STATUS_CREATED = 201
STATUS_SERVER_ERROR = 500


FORMAT = '%(levelname)s: %(asctime)s %(message)s'
logging.basicConfig(format=FORMAT,
                    filename='authentication/logging/modelsLogging.log',
                    level=logging.DEBUG)


class LoginView(View):

    """Class used to control the views from login of users."""

    http_method_names = [u'get', u'post']

    def get(self, request):
        """
        Returns all users.
        """

        logging.info("All users request")

        json_data = serialize_objects(BusinemeUser.objects.all())
        return JsonResponse(json_data, content_type='application/json')

    def get_user(self, user_id):
        """Return a user given a id"""

        try:
            user = BusinemeUser.objects.get(pk=user_id)
            json_data = serialize(user)
        except:
            json_data = return_message(STATUS_NOT_FOUND)

        return JsonResponse(json_data, content_type='application/json')
