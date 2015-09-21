"""
Busine-me API
Universidade de Brasilia - FGA
Técnicas de Programação, 2/2015
@file urls.py
File to route urls.
"""
from django.conf.urls import url
from .views import LoginView

urlpatterns = [
    url(r'^users/$', LoginView.as_view(),
        name='users'),
]
