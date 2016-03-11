# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
        ('accounts', '0006_trainingassistant_services'),
        ('schedules', '0002_auto_20151217_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(default=b'wor', max_length=3, choices=[(b'*', b'Star'), (b'*it', b'Star in training'), (b'os', b'Overseer'), (b'oa', b'Overseer Assistant'), (b'wor', b'Worker'), (b'vol', b'Volunteer'), (b'sub', b'Substitute'), (b'1st', b'1st timer')])),
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
            name='Instance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('event', models.ForeignKey(blank=True, to='schedules.Event', null=True)),
                ('period', models.ForeignKey(related_name='instances', to='services.Period')),
                ('service', models.ForeignKey(related_name='instances', to='services.Service')),
            ],
        ),
        migrations.CreateModel(
            name='LogEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=1, choices=[(b'd', b'debug'), (b'i', b'info'), (b'w', b'warning'), (b'e', b'error')])),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
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
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateField()),
                ('desc', models.TextField()),
                ('workload_margin', models.PositiveSmallIntegerField(default=2)),
                ('instances', models.ManyToManyField(to='ss.Instance')),
                ('period', models.ForeignKey(to='services.Period')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('workload', models.PositiveIntegerField()),
                ('weeks', models.PositiveSmallIntegerField()),
                ('account', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('designated', models.ManyToManyField(related_name='designated_workers', to='services.Service')),
                ('qualifications', models.ManyToManyField(to='ss.Qualification')),
                ('services_eligible', models.ManyToManyField(related_name='workers_eligible', to='ss.Instance')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkerGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=255)),
                ('workers', models.ManyToManyField(related_name='workergroups', null=True, to='accounts.Trainee', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='logevent',
            name='schedule',
            field=models.ForeignKey(related_name='log', to='ss.Schedule'),
        ),
        migrations.AddField(
            model_name='instance',
            name='workers',
            field=models.ManyToManyField(to='ss.Worker', null=True, through='ss.Assignment'),
        ),
        migrations.AddField(
            model_name='exception',
            name='trainees',
            field=models.ManyToManyField(related_name='exceptions', to='ss.Worker'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='instance',
            field=models.ForeignKey(to='ss.Instance'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='worker',
            field=models.ForeignKey(to='ss.Worker'),
        ),
    ]
