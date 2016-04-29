# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_auto_20160423_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roll',
            name='weekday',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
