# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seating', '0002_auto_20160515_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart',
            name='seats',
        ),
        migrations.AlterField(
            model_name='chart',
            name='desc',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
