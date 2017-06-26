# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^orders/$', views.order),
    url(r'^orderadd/$', views.orderadd),
]

