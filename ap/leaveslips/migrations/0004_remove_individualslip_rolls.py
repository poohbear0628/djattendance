# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaveslips', '0003_auto_20160507_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individualslip',
            name='rolls',
        ),
    ]
