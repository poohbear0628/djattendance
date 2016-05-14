# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160504_1806'),
        ('schedules', '0002_auto_20160504_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduletemplate',
            name='eventgroup',
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('schedules.event',),
        ),
        migrations.RemoveField(
            model_name='event',
            name='classs',
        ),
        migrations.RemoveField(
            model_name='event',
            name='group',
        ),
        migrations.RemoveField(
            model_name='event',
            name='term',
        ),
        migrations.AddField(
            model_name='event',
            name='class_type',
            field=models.CharField(blank=True, max_length=4, null=True, choices=[(b'MAIN', b'Main'), (b'1YR', b'1st Year'), (b'2YR', b'2nd Year'), (b'AFTN', b'Afternoon')]),
        ),
        migrations.AddField(
            model_name='event',
            name='day',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='weekday',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'Day of the week', choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b"Lord's Day")]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='comments',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 7, 13, 35, 58, 830822), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='import_to_next_term',
            field=models.BooleanField(default=False, verbose_name=b'Auto import schedule to the following term'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='schedule',
            name='name',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='priority',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='season',
            field=models.CharField(default=None, max_length=6, choices=[(b'Spring', b'Spring'), (b'Fall', b'Fall')]),
        ),
        migrations.AddField(
            model_name='schedule',
            name='trainees',
            field=models.ManyToManyField(related_name='schedules', to='accounts.Trainee', blank=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='weeks',
            field=models.CommaSeparatedIntegerField(default=[1], max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(max_length=1, choices=[(b'C', b'Class'), (b'S', b'Study'), (b'R', b'Rest'), (b'M', b'Meal'), (b'H', b'House'), (b'T', b'Team'), (b'L', b'Church Meeting'), (b'*', b'Special')]),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='events',
            field=models.ManyToManyField(related_name='schedules', to='schedules.Event', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set([]),
        ),
        migrations.DeleteModel(
            name='EventGroup',
        ),
        migrations.DeleteModel(
            name='ScheduleTemplate',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='term',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='trainee',
        ),
    ]
