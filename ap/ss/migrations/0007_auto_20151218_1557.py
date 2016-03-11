# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0006_worker_health'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='weeks',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='worker',
            name='workload',
            field=models.PositiveIntegerField(default=3),
        ),
    ]
