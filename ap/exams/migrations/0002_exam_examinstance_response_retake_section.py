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
                ('exam_template', models.ForeignKey(to='exams.Exam')),
                ('trainee', models.ForeignKey(to='accounts.Trainee')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('response_key', models.CharField(max_length=100, unique=True, serialize=False, primary_key=True)),
                ('response', django.contrib.postgres.fields.hstore.HStoreField(null=True)),
                ('grader_extra', django.contrib.postgres.fields.hstore.HStoreField(null=True)),
                ('score', models.DecimalField(max_digits=5, decimal_places=2)),
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
                ('template_section_key', models.CharField(max_length=100, unique=True, serialize=False, primary_key=True)),
                ('question_count', models.IntegerField()),
                ('first_question_index', models.IntegerField(default=1)),
                ('questions', django.contrib.postgres.fields.hstore.HStoreField(null=True)),
            ],
        ),
    ]
