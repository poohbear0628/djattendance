# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0009_roll_week'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roll',
            name='week',
        ),
        migrations.RemoveField(
            model_name='roll',
            name='weekday',
        ),
    ]
