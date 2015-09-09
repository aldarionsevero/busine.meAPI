from django.conf.urls import url
from .views import LoginView

urlpatterns = [
    url(r'^users/$', LoginView.as_view(),
        name='users'),
]
