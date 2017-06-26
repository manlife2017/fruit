# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        ('ttss', '0002_auto_20170623_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('cCount', models.IntegerField()),
                ('cGoods', models.ForeignKey(to='goods.GoodsInfo')),
                ('cUId', models.ForeignKey(related_name='user', to='ttss.UserInfo')),
            ],
        ),
    ]
