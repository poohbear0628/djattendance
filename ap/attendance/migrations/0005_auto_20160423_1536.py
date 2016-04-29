# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20160423_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='roll',
            name='day',
            field=models.DateField(default=datetime.datetime(2016, 4, 23, 15, 36, 27, 507025)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roll',
            name='timestart',
            field=models.TimeField(),
        ),
    ]
