# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect, HttpRequest


def login(func):
    def check_fun(request, *args, **kwargs):
        if request.session.get('u_id'):
            return func(request, *args, **kwargs)
        else:
            res = HttpResponseRedirect('/user/login/')
            res.set_cookie('url', request.get_full_path())
            return res
    return check_fun

