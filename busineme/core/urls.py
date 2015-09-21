from django.conf.urls import url
from .views import BuslineSearchResultView

urlpatterns = [
    url(r'^buslines/$', BuslineSearchResultView.as_view(),
        name='buslines'),
]
