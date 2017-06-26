from django.db import models
# from goods.models import *

# Create your models here.


# 用户UserInfo管理器
class UserInfoManager(models.Manager):
    def create(self, uname, uwd, ueamil, uaddress='', uphone='', ushou='',  isdelete=False, uyoubian=''):
        u = UserInfo()
        u.uname = uname
        u.upasswd = uwd
        u.ueamil = ueamil
        u.uaddress = uaddress
        u.uphone = uphone
        u.shou = ushou
        u.isdelete = isdelete
        u.uyoubian = uyoubian
        u.save()


# 用户UserInfo
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upasswd = models.CharField(max_length=40)
    uaddress = models.CharField(max_length=100)
    uphone = models.CharField(max_length=11)
    uyoubian = models.CharField(max_length=6)
    ushou = models.CharField(max_length=30)
    ueamil = models.CharField(max_length=30)
    isdelete = models.BooleanField(default=False)

    user = UserInfoManager()


# 购物车CartInfo
class CartInfo(models.Model):
    user = models.OneToOneField('UserInfo')
    # goods = models.
    count = models.IntegerField()


# 订单OrderInfo
class OrderInfo(models.Model):
    user = models.ForeignKey('UserInfo')
    # ototal
    state = models.ImageField()


# 订单详细OrderDetailInfo
# class OrderDetailInfo(models.Model):
#     order = models.CharField(max_length=30)
#     goods = models.ForeignKey('GoodsInfo')
#     count = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
