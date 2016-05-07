# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.hstore


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160504_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='BibleReading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weeklyReadingStatus', django.contrib.postgres.fields.hstore.HStoreField()),
                ('booksRead', django.contrib.postgres.fields.hstore.HStoreField()),
                ('trainee', models.ForeignKey(to='accounts.Trainee', null=True)),
            ],
        ),
    ]
