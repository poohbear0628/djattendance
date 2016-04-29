# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_auto_20160423_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roll',
            name='weekday',
            field=models.PositiveSmallIntegerField(verbose_name=b'Day of the week', choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b"Lord's Day")]),
        ),
    ]
