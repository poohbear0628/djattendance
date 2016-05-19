# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20160519_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='house',
            field=models.ForeignKey(blank=True, to='houses.House', null=True),
        ),
    ]
