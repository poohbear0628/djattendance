# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_auto_20160409_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='events',
            field=models.ManyToManyField(related_name='schedules', to='schedules.Event', blank=True),
        ),
    ]
