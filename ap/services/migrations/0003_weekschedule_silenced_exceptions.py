# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20160416_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekschedule',
            name='silenced_exceptions',
            field=models.ManyToManyField(to='services.Exception', verbose_name=b'Exceptions to ignore this week', blank=True),
        ),
    ]
