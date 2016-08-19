# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=1, choices=[(b'P', b'Present'), (b'A', b'Absent'), (b'T', b'Tardy'), (b'U', b'Uniform'), (b'L', b'Left Class')])),
                ('finalized', models.BooleanField(default=False)),
                ('notes', models.CharField(max_length=200, blank=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
