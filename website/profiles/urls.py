__author__ = 'soham'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sanders/$', views.index, name='sanders')
]