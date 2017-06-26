# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=30)),
                ('gimg', models.ImageField(upload_to='goods')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gmoods', models.IntegerField()),
                ('gunit', models.CharField(max_length=30)),
                ('gintroduce', models.CharField(max_length=60)),
                ('gdetails', tinymce.models.HTMLField()),
                ('grepertory', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=30)),
                ('isdelete', models.BooleanField(verbose_name=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='goods.TypeInfo'),
        ),
    ]
