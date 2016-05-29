# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aputils', '0004_auto_20160528_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='trainee',
            field=models.ForeignKey(related_name='vehicles', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
