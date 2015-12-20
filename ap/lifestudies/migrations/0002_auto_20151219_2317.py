# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifestudies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='due',
            field=models.DateTimeField(),
        ),
    ]
