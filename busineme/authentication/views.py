#!/usr/bin/env python
# coding: utf-8

"""Busine-me API

Universidade de Brasilia - FGA
Técnicas de Programação, 2/2015

@file views.py
Views (on classic MVC, controllers) with methods that control the requisitions for the user authentication and manipulation. 
"""

from django.views.generic import View
from django.utils.translation import ugettext as _
from core.serializers import serialize
from .models import BusinemeUser
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from core.return_message import return_message

STATUS_OK = 200
STATUS_NOT_FOUND = 404


class LoginView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        """Returns all users."""
        json_data = serialize('json', BusinemeUser.objects.all())
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request):
        """Verify if user exists and authenticates."""
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        json_data_user_authenticated = serialize('json', user)

        return HttpResponse(json_data_user_authenticated,
                            content_type='application/json')

    def delete(self, request):
        """Delete an user."""
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            user.delete()
            message_log = return_message(STATUS_OK)
            response = HttpResponse(
                message_log, content_type='application/json',
                status=STATUS_OK)
        else:
            message_log = return_message(STATUS_NOT_FOUND)
            response = HttpResponse(
                message_log, content_type='application/json',
                status=STATUS_NOT_FOUND)

        return response
