# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20160408_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='end',
            field=models.TimeField(default=datetime.datetime(2016, 4, 8, 16, 17, 36, 334235)),
        ),
        migrations.AlterField(
            model_name='service',
            name='start',
            field=models.TimeField(default=datetime.datetime(2016, 4, 8, 16, 17, 36, 334156)),
        ),
        migrations.AlterField(
            model_name='service',
            name='weekday',
            field=models.PositiveSmallIntegerField(default=b'5', max_length=1, choices=[(b'0', b'Monday'), (b'1', b'Tuesday'), (b'2', b'Wednesday'), (b'3', b'Thursday'), (b'4', b'Friday'), (b'5', b'Saturday'), (b'6', b"Lord's Day")]),
        ),
    ]
