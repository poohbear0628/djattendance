# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.hstore


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('accounts', '0006_trainingassistant_services'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(default=b'wor', max_length=3, choices=[(b'*', b'Star'), (b'*it', b'Star in training'), (b'os', b'Overseer'), (b'oa', b'Overseer Assistant'), (b'wor', b'Worker'), (b'vol', b'Volunteer'), (b'sub', b'Substitute'), (b'1st', b'1st timer')])),
                ('workload', models.PositiveSmallIntegerField(default=3)),
                ('gender', models.CharField(default=b'E', max_length=1, choices=[(b'B', b'Brother'), (b'S', b'Sister'), (b'E', b'Either'), (b'X', b'Either All Brothers or All Sisters')])),
                ('workers_required', models.PositiveSmallIntegerField(default=1)),
                ('pin', models.BooleanField(default=False)),
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
                ('services', models.ManyToManyField(to='services.Service')),
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
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('query', django.contrib.postgres.fields.hstore.HStoreField()),
            ],
        ),
        migrations.CreateModel(
            name='WeekSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateField()),
                ('desc', models.TextField()),
                ('workload_margin', models.PositiveSmallIntegerField(default=2)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('scheduler', models.ForeignKey(to='accounts.Trainee')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('health', models.PositiveIntegerField(default=10)),
                ('workload', models.PositiveIntegerField(default=3)),
                ('weeks', models.PositiveSmallIntegerField(default=1)),
                ('designated', models.ManyToManyField(related_name='designated_workers', to='services.Service', blank=True)),
                ('qualifications', models.ManyToManyField(to='ss.Qualification', blank=True)),
                ('services_eligible', models.ManyToManyField(related_name='workers_eligible', to='services.Service')),
                ('trainee', models.OneToOneField(to='accounts.Trainee')),
            ],
        ),
        migrations.CreateModel(
            name='WorkerGroup',
            fields=[
                ('group_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='auth.Group')),
                ('desc', models.CharField(max_length=255, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('query_filter', models.ForeignKey(related_name='filtered_workergroup', blank=True, to='ss.QueryFilter', null=True)),
                ('workers', models.ManyToManyField(related_name='workergroups', null=True, to='accounts.Trainee', blank=True)),
            ],
            bases=('auth.group',),
        ),
        migrations.AddField(
            model_name='exception',
            name='trainees',
            field=models.ManyToManyField(related_name='exceptions', to='ss.Worker'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='Week_schedule',
            field=models.ForeignKey(related_name='assignments', to='ss.WeekSchedule'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='service',
            field=models.ForeignKey(to='services.Service'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='service_worker_group',
            field=models.ForeignKey(to='ss.WorkerGroup'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='workers',
            field=models.ManyToManyField(related_name='assigned_services', to='ss.Worker', blank=True),
        ),
    ]
