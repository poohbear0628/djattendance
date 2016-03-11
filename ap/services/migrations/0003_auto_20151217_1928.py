# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20151217_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='category',
            field=models.ForeignKey(blank=True, to='services.Category', null=True),
        ),
        migrations.AlterField(
            model_name='period',
            name='workload',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='service',
            name='end',
            field=models.TimeField(default=datetime.time(19, 28, 41, 810818)),
        ),
        migrations.AlterField(
            model_name='service',
            name='start',
            field=models.TimeField(default=datetime.time(19, 28, 41, 810788)),
        ),
        migrations.AlterField(
            model_name='service',
            name='workers_required',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='service',
            name='workload',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
