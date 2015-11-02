"""
Busine-me API
Universidade de Brasilia - FGA
Técnicas de Programação, 2/2015
@file urls.py
File to route urls.
"""
from django.conf.urls import url
from .views import LoginView

"""
Defining the urls for the web application for the users page.
"""

urlpatterns = [
    url(r'^users/$', LoginView.as_view(),
        name='users'),
    url(r'^users/(?P<user_id>[0-9]+)/$', LoginView.get_user,
        name='users_id'),
]
