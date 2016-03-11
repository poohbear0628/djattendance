# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0003_auto_20151218_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='designated',
            field=models.ManyToManyField(related_name='designated_workers', to='services.Service', blank=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='qualifications',
            field=models.ManyToManyField(to='ss.Qualification', blank=True),
        ),
    ]
