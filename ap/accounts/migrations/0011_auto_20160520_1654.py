# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20160519_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='meta',
            field=models.OneToOneField(related_name='user', null=True, blank=True, to='accounts.UserMeta'),
        ),
    ]
