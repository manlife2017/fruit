# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartinfo',
            name='cUId',
            field=models.ForeignKey(to='ttss.UserInfo', related_name='cartuser'),
        ),
    ]
