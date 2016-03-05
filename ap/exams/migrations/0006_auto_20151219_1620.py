# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_auto_20151218_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='question_count',
            field=models.IntegerField(),
        ),
    ]
