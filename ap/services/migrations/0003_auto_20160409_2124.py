# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20160409_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='ScheduleCategory',
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(related_name='services', to='services.ServiceCategory'),
        ),
    ]
