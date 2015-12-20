# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150905_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latest_ls_chpt', models.CharField(max_length=400, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='trainee',
            name='statistics',
            field=models.OneToOneField(related_name='trainee', null=True, blank=True, to='accounts.Statistics'),
        ),
    ]
