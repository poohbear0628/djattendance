# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20160409_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workergroup',
            name='desc',
        ),
        migrations.AddField(
            model_name='workergroup',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
