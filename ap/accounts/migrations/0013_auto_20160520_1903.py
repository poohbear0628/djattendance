# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_user_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='term',
            new_name='terms_attended',
        ),
        migrations.AlterField(
            model_name='user',
            name='current_term',
            field=models.IntegerField(default=1, null=True, blank=True),
        ),
    ]
