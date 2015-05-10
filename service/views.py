from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
import json


class Serve(View):

    def get(self, request):

        data = {
            'request_ajax': request.is_ajax(),
            'request_body': request.GET.urlencode().split('&')
        }
        return HttpResponse(json.dumps(data), content_type='application/json')

class Show(TemplateView):
    template_name = 'index.html'