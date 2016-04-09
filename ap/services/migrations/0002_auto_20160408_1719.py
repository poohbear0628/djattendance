# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('ss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='worker_groups',
            field=models.ManyToManyField(to='ss.WorkerGroup', through='services.AssignmentPool'),
        ),
        migrations.AddField(
            model_name='seasonalserviceschedule',
            name='category',
            field=models.ForeignKey(blank=True, to='services.Category', null=True),
        ),
        migrations.AddField(
            model_name='assignmentpool',
            name='service',
            field=models.ForeignKey(to='services.Service'),
        ),
        migrations.AddField(
            model_name='assignmentpool',
            name='worker_group',
            field=models.ForeignKey(to='ss.WorkerGroup'),
        ),
    ]
