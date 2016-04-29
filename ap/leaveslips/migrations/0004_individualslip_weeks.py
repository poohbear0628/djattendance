# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaveslips', '0003_auto_20160316_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualslip',
            name='weeks',
            field=models.CommaSeparatedIntegerField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
