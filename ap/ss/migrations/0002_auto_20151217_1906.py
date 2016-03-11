# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='workers',
            field=models.ManyToManyField(to='ss.Worker', through='ss.Assignment'),
        ),
        migrations.AlterField(
            model_name='workergroup',
            name='workers',
            field=models.ManyToManyField(related_name='workergroups', to='accounts.Trainee', blank=True),
        ),
    ]
