# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150627_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingassistant',
            name='houses',
            field=models.ManyToManyField(to='houses.House', blank=True),
        ),
        migrations.AlterField(
            model_name='trainingassistant',
            name='services',
            field=models.ManyToManyField(to='services.Service', blank=True),
        ),
    ]
