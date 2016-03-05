# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_auto_20151129_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='question_count',
            field=models.IntegerField(default=0),
        ),
    ]
