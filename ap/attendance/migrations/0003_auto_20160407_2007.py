# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20160407_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roll',
            old_name='timestamp',
            new_name='last_modified',
        ),
    ]
