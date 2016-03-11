# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20151218_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='end',
            field=models.TimeField(default=datetime.datetime(2015, 12, 18, 15, 8, 27, 336387)),
        ),
        migrations.AlterField(
            model_name='service',
            name='start',
            field=models.TimeField(default=datetime.datetime(2015, 12, 18, 15, 8, 27, 336332)),
        ),
        migrations.AlterField(
            model_name='service',
            name='weekday',
            field=models.CharField(default=b'3', max_length=1, choices=[(b'0', b'Monday'), (b'1', b'Tuesday'), (b'2', b'Wednesday'), (b'3', b'Thursday'), (b'4', b'Friday'), (b'5', b'Saturday'), (b'6', b'Sunday')]),
        ),
    ]
