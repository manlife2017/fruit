from django.db import models
import sys
sys.path.append('..')
from goods.models import GoodsInfo
from ttss.models import UserInfo
# Create your models here.


class CartInfo(models.Model):
    cCount = models.IntegerField()
    cGoods = models.ForeignKey(GoodsInfo)
    cUId = models.ForeignKey(UserInfo, related_name='cartuser')
