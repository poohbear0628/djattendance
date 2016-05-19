# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20160518_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='trainee',
            field=models.OneToOneField(related_name='statistics', null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='house',
            field=models.ForeignKey(related_name='trainee', blank=True, to='houses.House', null=True),
        ),
    ]
