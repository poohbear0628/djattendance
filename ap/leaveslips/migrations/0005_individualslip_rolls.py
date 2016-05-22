# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_roll_date'),
        ('leaveslips', '0004_remove_individualslip_rolls'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualslip',
            name='rolls',
            field=models.ManyToManyField(related_name='leaveslips', to='attendance.Roll'),
        ),
    ]
