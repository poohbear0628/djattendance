# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20160409_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasonalserviceschedule',
            name='category',
            field=models.ForeignKey(default=1, to='services.ScheduleCategory'),
            preserve_default=False,
        ),
    ]
