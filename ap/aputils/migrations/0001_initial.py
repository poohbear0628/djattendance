# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models
import django_countries.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address1', models.CharField(max_length=150)),
                ('address2', models.CharField(max_length=150, blank=True)),
                ('zip_code', models.PositiveIntegerField(null=True, blank=True)),
                ('zip4', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('details', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('state', localflavor.us.models.USStateField(blank=True)),
                ('country', django_countries.fields.CountryField(default=b'US', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='EmergencyInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('relation', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('phone2', models.CharField(max_length=15, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='QueryFilter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('query', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=20, null=True, blank=True)),
                ('make', models.CharField(max_length=30, null=True, blank=True)),
                ('model', models.CharField(max_length=30, null=True, blank=True)),
                ('year', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('license_plate', models.CharField(max_length=25, null=True, blank=True)),
                ('state', localflavor.us.models.USStateField(blank=True)),
                ('capacity', models.PositiveSmallIntegerField()),
                ('user', models.ForeignKey(related_name='vehicles', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeAddress',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aputils.Address')),
            ],
            bases=('aputils.address',),
        ),
        migrations.AddField(
            model_name='emergencyinfo',
            name='address',
            field=models.ForeignKey(to='aputils.Address'),
        ),
    ]
