"""
Busine-me API
Universidade de Brasilia - FGA
Técnicas de Programação, 2/2015
@file views.py
Views (on classic MVC, controllers) with methods that control the requisitions
for the user authentication and manipulation.
"""

from django.views.generic import View
from core.serializers import serialize_objects
from core.serializers import serialize
from .models import Terminal
from .models import Busline
from django.http import JsonResponse
from core.return_message import return_message


STATUS_OK = 200
STATUS_CREATED = 201
STATUS_NOT_FOUND = 404
STATUS_SERVER_ERROR = 500

"""
This class is used for manage the results of Busline searchs.
"""


class BuslineSearchResultView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        """
        Returns all users.
        """
        filters = request.GET.dict()
        buslines = Busline.objects.filter(**filters)
        json_data = serialize_objects(buslines)
        return JsonResponse(json_data, content_type='application/json')

    def get_busline(self, busline_id):
        """
        Obtains the required busline based in line's number.
        """
        # busline = get_object_or_404(Busline, pk=busline_id)
        try:
            busline = Busline.objects.get(pk=busline_id)
            json_data = serialize(busline)
        except:
            json_data = return_message(STATUS_NOT_FOUND)
        return JsonResponse(json_data, content_type='application/json')


class TerminalSearchResultView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        """
        Returns all users.
        """
        filters = request.GET.dict()
        terminals = Terminal.objects.filter(**filters)
        json_data = serialize_objects(terminals)
        return JsonResponse(json_data, content_type='application/json')

    def get_terminal(self, terminal_id):
        """
        Obtains the required terminal based in line's number.
        """
        # terminal = get_object_or_404(terminal, pk=terminal_id)
        try:
            terminal = Terminal.objects.get(pk=terminal_id)
            json_data = serialize(terminal)
        except:
            json_data = return_message(STATUS_NOT_FOUND)
        return JsonResponse(json_data, content_type='application/json')
