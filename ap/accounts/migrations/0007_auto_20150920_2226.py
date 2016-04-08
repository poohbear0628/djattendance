# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20150919_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainee',
            name='statistics',
        ),
        migrations.AddField(
            model_name='statistics',
            name='trainee',
            field=models.OneToOneField(related_name='statistics', null=True, blank=True, to='accounts.Trainee'),
        ),
        migrations.AlterField(
            model_name='trainee',
            name='locality',
            field=models.ManyToManyField(to='localities.Locality', blank=True),
        ),
    ]
