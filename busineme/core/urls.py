"""
Busine-me API
Universidade de Brasilia - FGA
Tecnicas de Programacao, 2/2015
@file urls.py
File to route urls.
"""
from django.conf.urls import url
from .views import TerminalSearchResultView
from .views import BuslineSearchResultView
from .views import PostView


urlpatterns = [
    url(r'^buslines/$', BuslineSearchResultView.as_view(),
        name='buslines'),
    url(r'^buslines/(?P<busline_id>[0-9]+)/$',
        BuslineSearchResultView.get_busline),

    url(r'^terminals/$', TerminalSearchResultView.as_view(),
        name='terminals'),
    url(r'^terminals/(?P<terminal_id>[0-9]+)/$',
        TerminalSearchResultView.get_terminal),

    url(r'^posts/$', PostView.as_view(),
        name='posts'),
    url(r'^posts/(?P<post_id>[0-9]+)/$',
        PostView.get_post),

]
