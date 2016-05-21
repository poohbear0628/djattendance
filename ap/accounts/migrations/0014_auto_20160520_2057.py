# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20160520_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='meta',
        ),
        migrations.AddField(
            model_name='usermeta',
            name='user',
            field=models.OneToOneField(related_name='meta', null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(max_length=1, choices=[(b'T', b'Training Assistant'), (b'R', b'Regular (full-time)'), (b'S', b'Short-term (long-term)'), (b'C', b'Commuter')]),
        ),
    ]
