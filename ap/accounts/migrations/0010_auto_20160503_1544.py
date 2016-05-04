# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_trainee_office_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='date_begin',
            field=models.DateField(null=True, blank=True),
        ),
    ]
