# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seating', '0004_auto_20160521_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='desc',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
