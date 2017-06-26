from django.contrib import admin
from .models import *
# Register your models here.


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['ttitle']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['gtitle', 'gtype']
admin.site.register(GoodsInfo, GoodsInfoAdmin)
admin.site.register(TypeInfo, TypeInfoAdmin)
