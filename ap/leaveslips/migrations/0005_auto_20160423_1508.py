# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('leaveslips', '0004_individualslip_weeks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualslip',
            name='weeks',
            field=jsonfield.fields.JSONField(),
        ),
    ]
