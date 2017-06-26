# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^cart/$', views.cart),
    url(r'^add_(\d+)_(\d+)/$', views.add),
    url(r'^edit_(\d+)_(\d+)/$', views.edit),
    url(r'^del_(\d+)/$', views.delete)
]
