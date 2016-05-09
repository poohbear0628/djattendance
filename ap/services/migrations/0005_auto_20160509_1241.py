# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_remove_service_workers_required'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queryfilter',
            name='query',
        ),
        migrations.AlterField(
            model_name='queryfilter',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
