"""
Busine-me API
Universidade de Brasilia - FGA
Técnicas de Programação, 2/2015
@file urls.py
File to route urls.
"""
from django.conf.urls import url
from .views import BuslineSearchResultView

"""
Defining the urls for the web application for the buslines page.
"""

urlpatterns = [
    url(r'^buslines/$', BuslineSearchResultView.as_view(),
        name='buslines'),
    url(r'^buslines/(?P<line_number>[0-9]+)/$',
        BuslineSearchResultView.get_busline),
    url(r'^buslines/(?P<line_number>[0-9]+\.[0-9]+)/$',
        BuslineSearchResultView.get_busline),
    url(r'buslines/(?P<description>[a-z]+)/$',
        BuslineSearchResultView.get_description),
    url(r'buslines/(?P<description>[a-z]+\.[A-Z])/$',
        BuslineSearchResultView.get_description),
]
