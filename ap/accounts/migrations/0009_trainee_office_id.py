# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainee',
            name='office_id',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
    ]
