# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_roll'),
    ]

    operations = [
        migrations.AddField(
            model_name='roll',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 5, 7, 14, 0, 41, 749925)),
            preserve_default=False,
        ),
    ]
