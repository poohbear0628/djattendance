# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('isActive', models.BooleanField(default=True)),
                ('workload', models.IntegerField()),
                ('category', models.ForeignKey(to='services.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('group_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='auth.Group')),
                ('active', models.BooleanField(default=True)),
                ('designated', models.BooleanField()),
                ('gender', models.CharField(default=b'E', max_length=1, choices=[(b'B', b'Brother'), (b'S', b'Sister'), (b'E', b'Either')])),
                ('workload', models.PositiveSmallIntegerField()),
                ('workers_required', models.PositiveSmallIntegerField()),
                ('weekday', models.CharField(max_length=1, choices=[(b'0', b'Monday'), (b'1', b'Tuesday'), (b'2', b'Wednesday'), (b'3', b'Thursday'), (b'4', b'Friday'), (b'5', b'Saturday'), (b'6', b'Sunday')])),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('category', models.ForeignKey(related_name='services', to='services.Category')),
                ('period', models.ManyToManyField(related_name='services', to='services.Period')),
            ],
            bases=('auth.group',),
        ),
    ]
