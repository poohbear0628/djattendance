# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.hstore
from django.contrib.postgres.operations import HStoreExtension



class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='BibleReading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weekly_reading_status', django.contrib.postgres.fields.hstore.HStoreField()),
                ('books_read', django.contrib.postgres.fields.hstore.HStoreField()),
            ],
        ),
    ]
