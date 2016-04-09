# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20160408_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='end',
            field=models.TimeField(default=datetime.datetime(2016, 4, 8, 16, 26, 14, 668256)),
        ),
        migrations.AlterField(
            model_name='service',
            name='start',
            field=models.TimeField(default=datetime.datetime(2016, 4, 8, 16, 26, 14, 668225)),
        ),
        migrations.AlterField(
            model_name='service',
            name='weekday',
            field=models.PositiveSmallIntegerField(default=b'4', choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b"Lord's Day")]),
        ),
    ]
