# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('seating', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart',
            name='template',
        ),
        migrations.AddField(
            model_name='chart',
            name='height',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chart',
            name='seats',
            field=djorm_pgarray.fields.ArrayField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='chart',
            name='width',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Template',
        ),
    ]
