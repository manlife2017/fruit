# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttss', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsinfo',
            name='gtype',
        ),
        migrations.RemoveField(
            model_name='orderdetailinfo',
            name='goods',
        ),
        migrations.DeleteModel(
            name='GoodsInfo',
        ),
        migrations.DeleteModel(
            name='OrderDetailInfo',
        ),
        migrations.DeleteModel(
            name='TypeInfo',
        ),
    ]
