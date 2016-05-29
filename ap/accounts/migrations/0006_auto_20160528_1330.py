# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20160521_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermeta',
            old_name='married',
            new_name='is_couple',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='usermeta',
            name='spouse',
        ),
        migrations.AddField(
            model_name='user',
            name='is_hc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='office_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='college',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='degree',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='emergency_address',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='emergency_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='emergency_phone',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='emergency_phone2',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='gospel_pref1',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'CP', b'Campus'), (b'YP', b'Young People'), (b'CM', b'Community'), (b'CH', b'Children'), (b'ID', b'Internet Defense Confirmation Project')]),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='gospel_pref2',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'CP', b'Campus'), (b'YP', b'Young People'), (b'CM', b'Community'), (b'CH', b'Children'), (b'ID', b'Internet Defense Confirmation Project')]),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='home_phone',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='is_married',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='major',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='phone',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='readNT',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='readOT',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usermeta',
            name='work_phone',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
    ]
