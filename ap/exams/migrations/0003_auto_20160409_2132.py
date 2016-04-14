# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20160409_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='grade',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
    ]
