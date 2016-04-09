# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(max_length=1, choices=[(b'C', b'Class'), (b'S', b'Study'), (b'R', b'Rest'), (b'M', b'Meal'), (b'H', b'House'), (b'T', b'Team'), (b'L', b'Church Meeting'), (b'*', b'Special')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='week_day',
            field=models.PositiveSmallIntegerField(max_length=1, verbose_name=b'Day of the week', choices=[(b'0', b'Monday'), (b'1', b'Tuesday'), (b'2', b'Wednesday'), (b'3', b'Thursday'), (b'4', b'Friday'), (b'5', b'Saturday'), (b'6', b"Lord's Day")]),
        ),
    ]
