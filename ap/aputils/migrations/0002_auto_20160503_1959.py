# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aputils', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
