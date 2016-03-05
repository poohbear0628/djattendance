# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.hstore


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20150627_2125'),
        ('accounts', '0005_auto_20150905_1512'),
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_midterm', models.BooleanField()),
                ('section_count', models.IntegerField(default=1)),
                ('total_score', models.DecimalField(max_digits=5, decimal_places=2)),
                ('training_class', models.ForeignKey(to='classes.Class')),
            ],
        ),
        migrations.CreateModel(
            name='ExamInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_submitted_online', models.BooleanField(default=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('is_graded', models.BooleanField(default=False)),
                ('retake_number', models.IntegerField(default=0)),
                ('grade', models.IntegerField(default=0)),
                ('exam', models.ForeignKey(to='exams.Exam')),
                ('trainee', models.ForeignKey(to='accounts.Trainee')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_index', models.IntegerField(default=1)),
                ('response', django.contrib.postgres.fields.hstore.HStoreField(null=True)),
                ('grader_meta', django.contrib.postgres.fields.hstore.HStoreField(null=True)),
                ('score', models.DecimalField(max_digits=5, decimal_places=2)),
                ('instance', models.ForeignKey(to='exams.ExamInstance')),
                ('trainee', models.ForeignKey(to='accounts.Trainee')),
            ],
        ),
        migrations.CreateModel(
            name='Retake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('time_opened', models.DateTimeField(auto_now_add=True)),
                ('exam_template', models.ForeignKey(to='exams.Exam')),
                ('trainee', models.ForeignKey(to='accounts.Trainee')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_index', models.IntegerField(default=0)),
                ('first_question_index', models.IntegerField(default=1)),
                ('question_count', models.IntegerField()),
                ('questions', django.contrib.postgres.fields.hstore.HStoreField(null=True)),
                ('exam', models.ForeignKey(to='exams.Exam')),
            ],
        ),
    ]
