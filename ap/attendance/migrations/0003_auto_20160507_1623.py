# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160504_1806'),
        ('attendance', '0002_roll'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roll',
            old_name='timestamp',
            new_name='last_modified',
        ),
        migrations.RemoveField(
            model_name='roll',
            name='monitor',
        ),
        migrations.AddField(
            model_name='roll',
            name='submitted_by',
            field=models.ForeignKey(related_name='submitted_rolls', to='accounts.Trainee', null=True),
        ),
    ]
