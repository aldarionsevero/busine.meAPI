from django.conf.urls import include, url
from django.contrib import admin

"""
This code is used for detail the masters urls for the types
of users of aplications.
"""  

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('authentication.urls')),
    url(r'^', include('core.urls')),
]
