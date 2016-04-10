# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20160409_2124'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceCategory',
            new_name='Category',
        ),
    ]
