# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0011_auto_20160423_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roll',
            old_name='timestart',
            new_name='day',
        ),
    ]
