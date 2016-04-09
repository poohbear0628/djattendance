# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_auto_20160408_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='week_day',
        ),
        migrations.AddField(
            model_name='event',
            name='weekday',
            field=models.PositiveSmallIntegerField(default=1, verbose_name=b'Day of the week', choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b"Lord's Day")]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schedule',
            name='trainees',
            field=models.ManyToManyField(related_name='schedules', to='accounts.Trainee', blank=True),
        ),
    ]
