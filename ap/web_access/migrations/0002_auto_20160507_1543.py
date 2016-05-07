# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_access', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webrequest',
            options={'ordering': ['date_assigned', 'date_expire', 'trainee__firstname']},
        ),
    ]
