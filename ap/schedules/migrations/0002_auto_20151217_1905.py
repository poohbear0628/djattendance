# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgroup',
            name='repeat',
            field=models.CommaSeparatedIntegerField(max_length=13),
        ),
    ]
