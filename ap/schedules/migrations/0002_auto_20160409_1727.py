# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='repeat',
            field=models.CommaSeparatedIntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
