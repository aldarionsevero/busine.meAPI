"""
Busine-me API
Universidade de Brasilia - FGA
Técnicas de Programação, 2/2015
@file urls.py
File to route urls.
"""
from django.conf.urls import url
from .views import BuslineSearchResultView

urlpatterns = [
    url(r'^buslines/$', BuslineSearchResultView.as_view(),
        name='buslines'),
]
