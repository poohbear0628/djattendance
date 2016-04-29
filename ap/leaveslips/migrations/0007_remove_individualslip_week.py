# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaveslips', '0006_auto_20160423_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individualslip',
            name='week',
        ),
    ]
