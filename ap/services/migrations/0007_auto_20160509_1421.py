# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_queryfilter_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queryfilter',
            name='query',
            field=models.TextField(),
        ),
    ]
