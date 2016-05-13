# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20160509_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exception',
            old_name='trainees',
            new_name='workers',
        ),
    ]
