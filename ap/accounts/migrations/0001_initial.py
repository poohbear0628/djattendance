# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('type', models.CharField(max_length=1, choices=[(b'T', b'Training Assistant'), (b'R', b'Regular (full-time)'), (b'S', b'Short-term (long-term)'), (b'C', b'Commuter')])),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email address', db_index=True)),
                ('office_id', models.IntegerField(null=True, blank=True)),
                ('username', models.CharField(unique=True, validators=[django.core.validators.RegexValidator(b'^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', b'invalid')], error_messages={b'unique': 'A user with that username already exists.'}, max_length=30, blank=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', null=True, verbose_name='username')),
                ('firstname', models.CharField(max_length=30, verbose_name='first name')),
                ('lastname', models.CharField(max_length=30, verbose_name='last name')),
                ('middlename', models.CharField(max_length=30, null=True, verbose_name='middle name', blank=True)),
                ('nickname', models.CharField(max_length=30, null=True, blank=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'B', b'Brother'), (b'S', b'Sister')])),
                ('date_of_birth', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('current_term', models.IntegerField(default=1, null=True, blank=True)),
                ('date_begin', models.DateField(null=True, blank=True)),
                ('date_end', models.DateField(null=True, blank=True)),
                ('is_hc', models.BooleanField(default=False)),
                ('self_attendance', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['lastname', 'firstname'],
            },
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latest_ls_chpt', models.CharField(max_length=400, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=25, null=True, blank=True)),
                ('home_phone', models.CharField(max_length=25, null=True, blank=True)),
                ('work_phone', models.CharField(max_length=25, null=True, blank=True)),
                ('maidenname', models.CharField(max_length=30, null=True, verbose_name='maiden name', blank=True)),
                ('college', models.CharField(max_length=50, null=True, blank=True)),
                ('major', models.CharField(max_length=50, null=True, blank=True)),
                ('degree', models.CharField(max_length=30, null=True, blank=True)),
                ('emergency_name', models.CharField(max_length=100, null=True, blank=True)),
                ('emergency_address', models.CharField(max_length=250, null=True, blank=True)),
                ('emergency_phone', models.CharField(max_length=25, null=True, blank=True)),
                ('emergency_phone2', models.CharField(max_length=25, null=True, blank=True)),
                ('is_married', models.BooleanField(default=False)),
                ('is_couple', models.BooleanField(default=False)),
                ('gospel_pref1', models.CharField(blank=True, max_length=2, null=True, choices=[(b'CP', b'Campus'), (b'YP', b'Young People'), (b'CM', b'Community'), (b'CH', b'Children'), (b'ID', b'Internet Defense Confirmation Project')])),
                ('gospel_pref2', models.CharField(blank=True, max_length=2, null=True, choices=[(b'CP', b'Campus'), (b'YP', b'Young People'), (b'CM', b'Community'), (b'CH', b'Children'), (b'ID', b'Internet Defense Confirmation Project')])),
                ('readOT', models.BooleanField(default=False)),
                ('readNT', models.BooleanField(default=False)),
            ],
        ),
    ]
