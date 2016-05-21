# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seating', '0003_auto_20160521_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
