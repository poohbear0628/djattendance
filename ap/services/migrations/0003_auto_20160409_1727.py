# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('accounts', '0003_auto_20160408_1719'),
        ('services', '0002_auto_20160408_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentpool',
            name='service',
        ),
        migrations.RemoveField(
            model_name='seasonalserviceschedule',
            name='category',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='active',
            new_name='isActive',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='service',
            name='code',
        ),
        migrations.RemoveField(
            model_name='service',
            name='day',
        ),
        migrations.RemoveField(
            model_name='service',
            name='designated',
        ),
        migrations.RemoveField(
            model_name='service',
            name='end',
        ),
        migrations.RemoveField(
            model_name='service',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='service',
            name='id',
        ),
        migrations.RemoveField(
            model_name='service',
            name='name',
        ),
        migrations.RemoveField(
            model_name='service',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='service',
            name='start',
        ),
        migrations.RemoveField(
            model_name='service',
            name='weekday',
        ),
        migrations.RemoveField(
            model_name='service',
            name='workers_required',
        ),
        migrations.AddField(
            model_name='category',
            name='group_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=0, serialize=False, to='auth.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='group_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=0, serialize=False, to='auth.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='needQualification',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='need_qualification',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='qualifiedTrainees',
            field=models.ManyToManyField(to='accounts.Trainee', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='workload',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(blank=True, to='services.Category', null=True),
        ),
        migrations.DeleteModel(
            name='AssignmentPool',
        ),
        migrations.DeleteModel(
            name='SeasonalServiceSchedule',
        ),
    ]
