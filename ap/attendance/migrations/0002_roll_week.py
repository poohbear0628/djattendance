# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roll',
            name='week',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=False,
        ),
    ]
