# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20160409_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='weeks',
            field=models.PositiveSmallIntegerField(default=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='workergroup',
            name='workers',
            field=models.ManyToManyField(related_name='workergroups', to='services.Worker', blank=True),
        ),
    ]
