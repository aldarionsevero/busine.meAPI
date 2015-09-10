from django.views.generic import View
from django.utils.translation import ugettext as _
from core.serializers import serialize
from .models import BusinemeUser
from django.http import HttpResponse


class LoginView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        json_data = serialize('json', BusinemeUser.objects.all())
        return HttpResponse(json_data, content_type='application/json')
