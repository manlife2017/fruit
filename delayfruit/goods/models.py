from django.db import models
from tinymce.models import HTMLField

# Create your models here.


# 商品分类TypeInfo ttitle isDelete
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=30)
    isdelete = models.BooleanField(False)
    ttitle.short_description = '商品分别'

    def __str__(self):
        return self.ttitle


class GoodsInfoManager(models.Manager):

    def create(self, b):
        i = 0
        while i < 20:
            g = GoodsInfo()
            g.gtitle = '快速添加'+str(i)
            g.gtype = b
            g.gimg = 'goods/goods003.jpg'
            g.gprice = 16.80
            g.gmoods = 0
            g.gunit = '500g'
            g.gintroduce = '快速添加自作商品'+str(i)
            g.gdetails = '快速添加商品描述'+str(i)
            g.grepertory = 500
            g.isDelete = False
            g.save()
            i += 1


# 商品GoodsInfo
class GoodsInfo(models.Model):
    gtitle =models.CharField(max_length=30)
    gimg = models.ImageField(upload_to='goods')
    gtype = models.ForeignKey('TypeInfo')
    gprice = models.DecimalField(max_digits=10, decimal_places=2)
    gmoods = models.IntegerField()
    gunit = models.CharField(max_length=30)
    gintroduce = models.CharField(max_length=60)
    gdetails = HTMLField()
    grepertory = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    gtitle.short_description = '商品名'
    # good_create = GoodsInfoManager()

