# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_auto_20160504_1806'),
        ('services', '0002_auto_20160504_1806'),
        ('accounts', '0007_user_meta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='houses',
        ),
        migrations.RemoveField(
            model_name='user',
            name='services',
        ),
        migrations.AddField(
            model_name='usermeta',
            name='houses',
            field=models.ManyToManyField(related_name='houses', to='houses.House', blank=True),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='services',
            field=models.ManyToManyField(related_name='services', to='services.Service', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='meta',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usermeta',
            name='spouse',
            field=models.CharField(max_length=90, null=True, blank=True),
        ),
    ]
