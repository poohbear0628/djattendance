# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localities', '0002_locality_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locality',
            name='country',
        ),
    ]
