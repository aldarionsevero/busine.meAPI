"""Busine-me API
Universidade de Brasilia - FGA
Técnicas de Programação, 2/2015
@file views.py
Views (on classic MVC, controllers) with methods that control the requisitions
for the user authentication and manipulation.
"""

from django.views.generic import View
from core.serializers import serialize_objects
from .models import Busline
from django.http import JsonResponse

STATUS_OK = 200
STATUS_NOT_FOUND = 404
STATUS_CREATED = 201
STATUS_SERVER_ERROR = 500


class BuslineSearchResultView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        """Returns all users."""
        json_data = serialize_objects(Busline.objects.all())
        return JsonResponse(json_data, content_type='application/json')

    def get_busline(self, line_number):

        busline = Busline.api_filter_startswith(line_number)
        json_data = serialize_objects(busline)

        return JsonResponse(json_data, content_type='application/json')

    def get_description(self, description):

        busline = Busline.filter_by_description(description)
        json_data_buslines_description = serialize_objects(busline)

        return JsonResponse(json_data_buslines_description,
                            content_type='application/json')
