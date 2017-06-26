# -*- coding:utf-8 -*-
from django.conf.urls import url
from .models import *
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^search/$', views.MySearchView()),
    url(r'^(\d+)/$', views.detail),
    url(r'^list_(\d+)_(\d+)_(\d+)/$', views.list),
]

