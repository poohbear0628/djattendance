# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentPool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workers_required', models.PositiveSmallIntegerField(default=1)),
                ('workload', models.PositiveSmallIntegerField(default=3)),
                ('role', models.CharField(default=b'wor', max_length=3, choices=[(b'*', b'Star'), (b'*it', b'Star in training'), (b'os', b'Overseer'), (b'oa', b'Overseer Assistant'), (b'wor', b'Worker'), (b'vol', b'Volunteer'), (b'sub', b'Substitute'), (b'1st', b'1st timer')])),
                ('gender', models.CharField(default=b'E', max_length=1, choices=[(b'B', b'Brother'), (b'S', b'Sister'), (b'E', b'Either'), (b'X', b'Either All Brothers or All Sisters')])),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SeasonalServiceSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('designated', models.BooleanField(default=False)),
                ('gender', models.CharField(default=b'E', max_length=1, choices=[(b'B', b'Brother'), (b'S', b'Sister'), (b'E', b'Either'), (b'X', b'Either All Brothers or All Sisters')])),
                ('workers_required', models.PositiveSmallIntegerField(default=1)),
                ('weekday', models.CharField(default=b'7', max_length=1, choices=[(b'0', b'Monday'), (b'1', b'Tuesday'), (b'2', b'Wednesday'), (b'3', b'Thursday'), (b'4', b'Friday'), (b'5', b'Saturday'), (b'6', b"Lord's Day")])),
                ('start', models.TimeField(default=datetime.datetime(2016, 4, 8, 16, 1, 1, 635249))),
                ('end', models.TimeField(default=datetime.datetime(2016, 4, 8, 16, 1, 1, 635284))),
                ('day', models.DateField(null=True, blank=True)),
                ('category', models.ForeignKey(related_name='services', to='services.Category')),
                ('schedule', models.ManyToManyField(related_name='services', to='services.SeasonalServiceSchedule')),
            ],
        ),
    ]
