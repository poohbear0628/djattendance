# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_trainingassistant_services'),
        ('ss', '0002_auto_20151217_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='account',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='active',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='date_created',
        ),
        migrations.AddField(
            model_name='worker',
            name='trainee',
            field=models.OneToOneField(default=1, to='accounts.Trainee'),
            preserve_default=False,
        ),
    ]
