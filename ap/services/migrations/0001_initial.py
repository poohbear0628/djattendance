# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('accounts', '0012_auto_20160725_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pin', models.BooleanField(default=False)),
                ('workload', models.PositiveSmallIntegerField(default=1)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentPool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workers_required', models.PositiveSmallIntegerField(default=1)),
                ('workload', models.PositiveSmallIntegerField(default=3)),
                ('role', models.CharField(default=b'wor', max_length=3, choices=[(b'*', b'Star'), (b'*it', b'Star in training'), (b'os', b'Overseer'), (b'oa', b'Overseer Assistant'), (b'wor', b'Worker'), (b'vol', b'Volunteer'), (b'sub', b'Substitute'), (b'1st', b'1st timer')])),
                ('gender', models.CharField(default=b'E', max_length=1, choices=[(b'B', b'Brother'), (b'S', b'Sister'), (b'E', b'Either'), (b'X', b'Either All Brothers or All Sisters')])),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exception',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=255)),
                ('start', models.DateField()),
                ('end', models.DateField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QueryFilter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('query', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeasonalServiceSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(to='services.ScheduleCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('designated', models.BooleanField(default=False)),
                ('gender', models.CharField(default=b'E', max_length=1, choices=[(b'B', b'Brother'), (b'S', b'Sister'), (b'E', b'Either'), (b'X', b'Either All Brothers or All Sisters')])),
                ('weekday', models.PositiveSmallIntegerField(choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b"Lord's Day")])),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('day', models.DateField(null=True, blank=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(related_name='services', to='services.Category')),
                ('schedule', models.ManyToManyField(related_name='services', to='services.SeasonalServiceSchedule')),
            ],
        ),
        migrations.CreateModel(
            name='WeekSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateField()),
                ('description', models.TextField(null=True, blank=True)),
                ('workload_margin', models.PositiveSmallIntegerField(default=2)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('scheduler', models.ForeignKey(to='accounts.Trainee')),
                ('silenced_exceptions', models.ManyToManyField(to='services.Exception', verbose_name=b'Exceptions to ignore this week', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('health', models.PositiveIntegerField(default=10)),
                ('services_cap', models.PositiveSmallIntegerField(default=3)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('designated', models.ManyToManyField(related_name='designated_workers', to='services.Service', blank=True)),
                ('qualifications', models.ManyToManyField(to='services.Qualification', blank=True)),
                ('services_eligible', models.ManyToManyField(related_name='workers_eligible', to='services.Service', blank=True)),
                ('trainee', models.OneToOneField(to='accounts.Trainee')),
            ],
        ),
        migrations.CreateModel(
            name='WorkerGroup',
            fields=[
                ('group_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='auth.Group')),
                ('description', models.TextField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('query_filter', models.ForeignKey(related_name='filtered_workergroup', blank=True, to='services.QueryFilter', null=True)),
                ('workers', models.ManyToManyField(related_name='workergroups', to='services.Worker', blank=True)),
            ],
            bases=('auth.group',),
        ),
        migrations.AddField(
            model_name='service',
            name='worker_groups',
            field=models.ManyToManyField(to='services.WorkerGroup', through='services.AssignmentPool'),
        ),
        migrations.AddField(
            model_name='exception',
            name='services',
            field=models.ManyToManyField(to='services.Service'),
        ),
        migrations.AddField(
            model_name='exception',
            name='workers',
            field=models.ManyToManyField(related_name='exceptions', to='services.Worker'),
        ),
        migrations.AddField(
            model_name='assignmentpool',
            name='service',
            field=models.ForeignKey(to='services.Service'),
        ),
        migrations.AddField(
            model_name='assignmentpool',
            name='worker_group',
            field=models.ForeignKey(to='services.WorkerGroup'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='pool',
            field=models.ForeignKey(to='services.AssignmentPool'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='service',
            field=models.ForeignKey(related_name='assignments', to='services.Service'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='week_schedule',
            field=models.ForeignKey(related_name='assignments', to='services.WeekSchedule'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='workers',
            field=models.ManyToManyField(related_name='assignments', to='services.Worker', blank=True),
        ),
    ]
