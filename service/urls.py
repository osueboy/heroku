__author__ = 'osueboy'

from django.conf.urls import include, url
from views import Serve, Show
urlpatterns = [
    url(r'api/$', Serve.as_view(), name='service'),
    url(r'$', Show.as_view(), name='show'),


]