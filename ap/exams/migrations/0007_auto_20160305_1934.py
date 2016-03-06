# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_auto_20151219_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='responses',
            old_name='instance',
            new_name='session',
        ),
    ]
