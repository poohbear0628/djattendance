# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160504_1806'),
        ('services', '0002_auto_20160504_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='service',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AddField(
            model_name='service',
            name='needQualification',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='need_qualification',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='qualifiedTrainees',
            field=models.ManyToManyField(to='accounts.Trainee', blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(blank=True, to='services.Category', null=True),
        ),
        migrations.DeleteModel(
            name='Period',
        ),
    ]
