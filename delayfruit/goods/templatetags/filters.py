# -*- coding:utf-8 -*-
from django.template import Library
register = Library()


@register.filter
def tostr(value):
    return str(value)
