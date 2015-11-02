"""
Busine-me API
Universidade de Brasilia - FGA
Técnicas de Programação, 2/2015
@file urls.py
File to route urls.
"""
from django.conf.urls import url
from .views import TerminalSearchResultView
from .views import BuslineSearchResultView

"""
Defining the urls for the web application for the buslines page.
"""

urlpatterns = [
    url(r'^buslines/$', BuslineSearchResultView.as_view(),
        name='buslines'),
    url(r'^buslines/(?P<busline_id>[0-9]+)/$',
        BuslineSearchResultView.get_busline),

    url(r'^terminals/$', TerminalSearchResultView.as_view(),
        name='terminals'),
    url(r'^terminals/(?P<terminal_id>[0-9]+)/$',
        TerminalSearchResultView.get_terminal),

]
