# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial')
    ]

    operations = [
        migrations.AddField(
            model_name='seasonalserviceschedule',
            name='category',
            field=models.ForeignKey(blank=True, to='services.Category', null=True),
        ),
        migrations.AddField(
            model_name='assignmentpool',
            name='service',
            field=models.ForeignKey(to='services.Service'),
        )
    ]
