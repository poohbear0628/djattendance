# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0004_auto_20151218_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='weeks',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
