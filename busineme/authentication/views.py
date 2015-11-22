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
from django.contrib.auth import authenticate
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

"""
Class used to control the views from login of users.
"""


class LoginView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        """
        Returns all users.
        """

        logging.info("All users request")

        json_data = serialize_objects(BusinemeUser.objects.all())
        return JsonResponse(json_data, content_type='application/json')

    def get_user(self, request, user_id):
        """Return a user given a id"""

        try:
            user = BusinemeUser.objects.get(pk=user_id)
            json_data = serialize(user)
        except:
            json_data = return_message(STATUS_NOT_FOUND)

        return JsonResponse(json_data, content_type='application/json')

    def post(self, request):
        """
        Verify if user exists and authenticates.
        """

        logging.info("create new user request")

        new_user = BusinemeUser()
        new_user.create_user(request)
        user = new_user.user_authenticate(request)

        if user is not None:
            message_log = return_message(STATUS_CREATED)
            response = JsonResponse(
                message_log, content_type='application/json',
                status=STATUS_CREATED)
        else:
            message_log = return_message(STATUS_SERVER_ERROR)
            response = JsonResponse(
                message_log, content_type='application/json',
                status=STATUS_SERVER_ERROR)

        return response

    def delete(self, request):
        """
        Delete an user.
        """

        logging.info("delete user requested")

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            user.delete()
            message_log = return_message(STATUS_OK)
            response = JsonResponse(
                message_log, content_type='application/json',
                status=STATUS_OK)
        else:
            message_log = return_message(STATUS_NOT_FOUND)
            response = JsonResponse(
                message_log, content_type='application/json',
                status=STATUS_NOT_FOUND)

        return response
