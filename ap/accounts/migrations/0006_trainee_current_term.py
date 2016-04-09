# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150905_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainee',
            name='current_term',
            field=models.IntegerField(default=1),
        ),
    ]
