# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.hstore


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20160509_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='queryfilter',
            name='query',
            field=django.contrib.postgres.fields.hstore.HStoreField(default={}),
            preserve_default=False,
        ),
    ]
