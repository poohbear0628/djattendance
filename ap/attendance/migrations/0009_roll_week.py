# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_auto_20160423_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='roll',
            name='week',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
