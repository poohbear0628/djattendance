# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import paintstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BadgePrintSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('banner_color', paintstore.fields.ColorPickerField(max_length=7)),
            ],
            options={
                'verbose_name': 'Badge Printing Configuration',
            },
        ),
        migrations.AddField(
            model_name='badge',
            name='deactivated',
            field=models.BooleanField(default=False),
        ),
    ]
