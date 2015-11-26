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
from .models import Terminal
from .models import Busline
from .models import Post
from .models import Favorite
from django.http import JsonResponse
from core.return_message import return_message


STATUS_OK = 200
STATUS_CREATED = 201
STATUS_NOT_FOUND = 404
STATUS_SERVER_ERROR = 500


class BuslineSearchResultView(View):

    """This class is used for manage the results of Busline searchs."""

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
        try:
            busline = Busline.objects.get(pk=busline_id)
            json_data = serialize(busline)
        except Busline.DoesNotExist:
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

        try:
            terminal = Terminal.objects.get(pk=terminal_id)
            json_data = serialize(terminal)
        except Terminal.DoesNotExist:
            json_data = return_message(STATUS_NOT_FOUND)
        return JsonResponse(json_data, content_type='application/json')


class PostView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        """
        Returns posts.
        """

        filters = request.GET.dict()
        posts = Post.objects.filter(**filters)
        json_data = serialize_objects(posts)
        return JsonResponse(json_data, content_type='application/json')

    def get_post(self, post_id):
        """
        Obtains the required terminal based in line's number.
        """

        try:
            post = Post.objects.get(pk=post_id)
            json_data = serialize(post)
        except Post.DoesNotExist:
            json_data = return_message(STATUS_NOT_FOUND)
        return JsonResponse(json_data, content_type='application/json')


class FavoriteView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        """
        Generate a new favorite if the search in db return nothing.
        If the db return something this favorite is deleted.
        """

        user = request.POST['user']
        busline = request.POST['busline']

        favorite = Favorite.objects.get(user=user, busline=busline)

        if(favorite is not None):
            new_favorite = Favorite()

            new_favorite.user = user
            new_favorite.busline = busline
            new_favorite.save()

        else:
            favorite.delete()
