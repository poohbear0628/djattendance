# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20160513_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='meta',
            field=models.ForeignKey(blank=True, to='accounts.UserMeta', null=True),
        ),
    ]
