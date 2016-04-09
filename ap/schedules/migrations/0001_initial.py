# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=250, blank=True)),
                ('type', models.CharField(max_length=1, choices=[(b'C', b'Class'), (b'S', b'Study'), (b'M', b'Meal'), (b'H', b'House'), (b'T', b'Team'), (b'L', b'Church Meeting'), (b'*', b'Special')])),
                ('class_type', models.CharField(blank=True, max_length=4, null=True, choices=[(b'MAIN', b'Main'), (b'1YR', b'1st Year'), (b'2YR', b'2nd Year'), (b'AFTN', b'Afternoon')])),
                ('monitor', models.CharField(blank=True, max_length=2, null=True, choices=[(b'AM', b'Attendance Monitor'), (b'TM', b'Team Monitor'), (b'HC', b'House Coordinator')])),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('day', models.DateField(null=True, blank=True)),
                ('week_day', models.PositiveSmallIntegerField(verbose_name=b'Day of the week', choices=[(b'0', b'Monday'), (b'1', b'Tuesday'), (b'2', b'Wednesday'), (b'3', b'Thursday'), (b'4', b'Friday'), (b'5', b'Saturday'), (b'6', b"Lord's Day")])),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('comments', models.CharField(max_length=250, blank=True)),
                ('priority', models.SmallIntegerField()),
                ('weeks', models.CommaSeparatedIntegerField(max_length=50)),
                ('season', models.CharField(default=None, max_length=6, choices=[(b'Spring', b'Spring'), (b'Fall', b'Fall')])),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('import_to_next_term', models.BooleanField(default=False, verbose_name=b'Auto import schedule to the following term')),
                ('is_deleted', models.BooleanField(default=False)),
                ('events', models.ManyToManyField(to='schedules.Event', blank=True)),
                ('trainees', models.ManyToManyField(related_name='schedules', null=True, to='accounts.Trainee', blank=True)),
            ],
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
    ]
