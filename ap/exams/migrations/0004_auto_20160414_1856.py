# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20160409_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='grade',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
        ),
    ]
