# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20160528_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermeta',
            name='emergency_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
