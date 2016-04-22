# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_roll_week'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roll',
            name='week',
        ),
        migrations.AddField(
            model_name='roll',
            name='timestart',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 20, 6, 41, 885331), auto_now=True),
            preserve_default=False,
        ),
    ]
