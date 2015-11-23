"""
Busine-me API
Universidade de Brasilia - FGA
Tecnicas de Programacao, 2/2015
@file urls.py
File to route urls.
"""
from django.conf.urls import url
from .views import LoginView

urlpatterns = [
    url(r'^users/$', LoginView.as_view(),
        name='users'),
    url(r'^users/(?P<user_id>[0-9]+)/$', LoginView.get_user,
        name='users_id'),
]
