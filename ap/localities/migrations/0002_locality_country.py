# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('localities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locality',
            name='country',
            field=django_countries.fields.CountryField(default='US', max_length=2),
            preserve_default=False,
        ),
    ]
