# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
