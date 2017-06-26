from django.contrib import admin
from .models import OrderInfo, OrderDetails
# Register your models here.
admin.site.register(OrderInfo)
admin.site.register(OrderDetails)
