# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20151128_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='section_count',
        ),
        migrations.AddField(
            model_name='exam',
            name='is_open',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exam',
            name='total_score',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='section',
            name='exam',
            field=models.ForeignKey(related_name='sections', to='exams.Exam'),
        ),
    ]
