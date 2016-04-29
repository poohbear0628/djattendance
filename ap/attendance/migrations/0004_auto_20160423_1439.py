# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20160414_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roll',
            name='timestart',
            field=models.DateTimeField(),
        ),
    ]
