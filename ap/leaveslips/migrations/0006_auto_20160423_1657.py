# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaveslips', '0005_auto_20160423_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individualslip',
            old_name='weeks',
            new_name='week',
        ),
    ]
