from django.db import models
import sys
sys.path.append('..')
from ttss.models import UserInfo
from goods.models import GoodsInfo
# Create your models here.


class OrderInfo(models.Model):
    ouser = models.ForeignKey(UserInfo, related_name='orderuser')
    ostate = models.IntegerField(default=0)
    odate = models.DateTimeField(auto_now=True)
    oprice = models.DecimalField(max_digits=10, decimal_places=2)
    # class Meta(object):
    #     db_table = 'order'


class OrderDetails(models.Model):
    order = models.ForeignKey(OrderInfo)
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
    price = models.IntegerField()
