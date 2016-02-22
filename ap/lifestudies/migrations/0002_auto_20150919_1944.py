# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifestudies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discipline',
            options={'ordering': ['trainee__account__lastname']},
        ),
        migrations.AddField(
            model_name='discipline',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
