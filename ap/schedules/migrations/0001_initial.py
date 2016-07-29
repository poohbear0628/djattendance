# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terms', '0001_initial'),
        ('teams', '0001_initial'),
        ('aputils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=250, blank=True)),
                ('type', models.CharField(max_length=1, choices=[(b'C', b'Class'), (b'S', b'Study'), (b'R', b'Rest'), (b'M', b'Meal'), (b'H', b'House'), (b'T', b'Team'), (b'Y', b'YPC'), (b'L', b'Church Meeting'), (b'*', b'Special')])),
                ('class_type', models.CharField(blank=True, max_length=4, null=True, choices=[(b'MAIN', b'Main'), (b'1YR', b'1st Year'), (b'2YR', b'2nd Year'), (b'AFTN', b'Afternoon')])),
                ('monitor', models.CharField(blank=True, max_length=2, null=True, choices=[(b'AM', b'Attendance Monitor'), (b'TM', b'Team Monitor'), (b'HC', b'House Coordinator')])),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('day', models.DateField(null=True, blank=True)),
                ('weekday', models.PositiveSmallIntegerField(verbose_name=b'Day of the week', choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b"Lord's Day")])),
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
                ('season', models.CharField(default=None, max_length=6, choices=[(b'Spring', b'Spring'), (b'Fall', b'Fall'), (b'All', b'All')])),
                ('trainee_select', models.CharField(max_length=2, choices=[(b'MC', b'Main Classroom'), (b'FY', b'First Year'), (b'SY', b'Second Year'), (b'TE', b'Team'), (b'YP', b'YP'), (b'CH', b'Children'), (b'MA', b'Manual')])),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('import_to_next_term', models.BooleanField(default=False, verbose_name=b'Auto import schedule to the following term')),
                ('is_locked', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('events', models.ManyToManyField(related_name='schedules', to='schedules.Event', blank=True)),
                ('parent_schedule', models.ForeignKey(related_name='parent', blank=True, to='schedules.Schedule', null=True)),
                ('query_filter', models.ForeignKey(blank=True, to='aputils.QueryFilter', null=True)),
                ('team_roll', models.ForeignKey(related_name='schedules', blank=True, to='teams.Team', null=True)),
                ('term', models.ForeignKey(blank=True, to='terms.Term', null=True)),
            ],
            options={
                'ordering': ('priority', 'season'),
            },
        ),
    ]
