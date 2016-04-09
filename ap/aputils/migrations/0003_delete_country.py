# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aputils', '0002_auto_20151114_2048'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Country',
        ),
    ]
