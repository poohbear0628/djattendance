# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('terms', '0002_term'),
        ('accounts', '0005_trainee_current_term'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Partial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x_lower', models.SmallIntegerField()),
                ('x_upper', models.SmallIntegerField()),
                ('y_lower', models.SmallIntegerField()),
                ('y_upper', models.SmallIntegerField()),
                ('chart', models.ForeignKey(to='seating.Chart')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.SmallIntegerField()),
                ('y', models.SmallIntegerField()),
                ('chart', models.ForeignKey(to='seating.Chart')),
                ('trainee', models.ForeignKey(to='accounts.Trainee')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=255)),
                ('height', models.PositiveSmallIntegerField()),
                ('width', models.PositiveSmallIntegerField()),
                ('seats', djorm_pgarray.fields.ArrayField(default=None, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='chart',
            name='template',
            field=models.ForeignKey(to='seating.Template'),
        ),
        migrations.AddField(
            model_name='chart',
            name='term',
            field=models.ForeignKey(to='terms.Term'),
        ),
        migrations.AddField(
            model_name='chart',
            name='trainees',
            field=models.ManyToManyField(to='accounts.Trainee', through='seating.Seat'),
        ),
    ]
