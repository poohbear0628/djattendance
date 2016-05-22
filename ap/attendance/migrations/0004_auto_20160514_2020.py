# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_roll_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roll',
            old_name='monitor',
            new_name='submitted_by',
        ),
    ]
