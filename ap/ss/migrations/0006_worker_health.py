# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0005_auto_20151218_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='health',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
