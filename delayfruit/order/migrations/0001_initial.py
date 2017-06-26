# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttss', '0002_auto_20170623_2020'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('goods', models.ForeignKey(to='goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('ostate', models.IntegerField(default=0)),
                ('odate', models.DateTimeField(auto_now=True)),
                ('oprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ouser', models.ForeignKey(related_name='orderuser', to='ttss.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='order',
            field=models.ForeignKey(to='order.OrderInfo'),
        ),
    ]
