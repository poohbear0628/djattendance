# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaveslips', '0002_auto_20160305_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupslip',
            name='TA',
            field=models.ForeignKey(blank=True, to='accounts.TrainingAssistant', null=True),
        ),
        migrations.AlterField(
            model_name='individualslip',
            name='TA',
            field=models.ForeignKey(blank=True, to='accounts.TrainingAssistant', null=True),
        ),
    ]
