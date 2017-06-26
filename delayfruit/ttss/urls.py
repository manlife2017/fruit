# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/register/$', views.register),
    url(r'^user/user_add/$', views.user_add),
    url(r'^user/login/$', views.login),
    url(r'^user/check_u/$', views.check_u),
    url(r'^user/info/$', views.info),
    url(r'^user/order(\d*)/$', views.order),
    url(r'^user/site/$', views.site),
    url(r'^user/quit/$', views.quit),
]
