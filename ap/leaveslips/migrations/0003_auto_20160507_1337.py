# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_roll'),
        ('leaveslips', '0002_groupslip_individualslip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individualslip',
            name='events',
        ),
        migrations.AddField(
            model_name='individualslip',
            name='rolls',
            field=models.ManyToManyField(related_name='leaveslips', to='attendance.Roll'),
        ),
        migrations.AlterField(
            model_name='groupslip',
            name='TA',
            field=models.ForeignKey(blank=True, to='accounts.TrainingAssistant', null=True),
        ),
        migrations.AlterField(
            model_name='groupslip',
            name='trainee',
            field=models.ForeignKey(related_name='groupslips', to='accounts.Trainee'),
        ),
        migrations.AlterField(
            model_name='individualslip',
            name='TA',
            field=models.ForeignKey(blank=True, to='accounts.TrainingAssistant', null=True),
        ),
        migrations.AlterField(
            model_name='individualslip',
            name='trainee',
            field=models.ForeignKey(related_name='individualslips', to='accounts.Trainee'),
        ),
    ]
