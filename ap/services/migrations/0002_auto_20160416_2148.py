# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='services_eligible',
            field=models.ManyToManyField(related_name='workers_eligible', to='services.Service', blank=True),
        ),
    ]
