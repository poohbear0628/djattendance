# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '__first__'),
        ('accounts', '0003_auto_20150530_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainee',
            name='badge',
            field=models.ForeignKey(blank=True, to='badges.Badge', null=True),
        ),
        migrations.AddField(
            model_name='trainingassistant',
            name='badge',
            field=models.ForeignKey(blank=True, to='badges.Badge', null=True),
        ),
        migrations.AlterField(
            model_name='trainingassistant',
            name='houses',
            field=models.ManyToManyField(to='houses.House', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='trainingassistant',
            name='services',
            field=models.ManyToManyField(to='services.Service', null=True, blank=True),
        ),
    ]
