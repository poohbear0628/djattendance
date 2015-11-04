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
                ('is_submitted_online', models.BooleanField(default=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('is_graded', models.BooleanField(default=False)),
                ('retake_number', models.IntegerField(default=0)),
                ('grade', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ExamResponse',
            fields=[
                ('response_key', models.CharField(max_length=100, unique=True, serialize=False, primary_key=True)),
                ('response', models.CharField(max_length=10000)),
                ('score', models.IntegerField(null=True, blank=True)),
                ('grader_extra', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ExamRetake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('time_opened', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExamTemplateDescriptor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opens_on', models.DateTimeField()),
                ('closes_on', models.DateTimeField()),
                ('is_midterm', models.BooleanField()),
                ('section_count', models.IntegerField(default=1)),
                ('total_score', models.IntegerField(default=1)),
                ('training_class', models.ForeignKey(to='classes.Class')),
            ],
        ),
        migrations.CreateModel(
            name='ExamTemplateSections',
            fields=[
                ('template_section_key', models.CharField(max_length=100, unique=True, serialize=False, primary_key=True)),
                ('question_count', models.IntegerField()),
                ('first_question_index', models.IntegerField(default=1)),
                ('questions', django.contrib.postgres.fields.hstore.HStoreField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='examretake',
            name='exam_template',
            field=models.ForeignKey(to='exams.ExamTemplateDescriptor'),
        ),
        migrations.AddField(
            model_name='examretake',
            name='trainee',
            field=models.ForeignKey(to='accounts.Trainee'),
        ),
        migrations.AddField(
            model_name='exam',
            name='exam_template',
            field=models.ForeignKey(to='exams.ExamTemplateDescriptor'),
        ),
        migrations.AddField(
            model_name='exam',
            name='trainee',
            field=models.ForeignKey(to='accounts.Trainee'),
        ),
    ]
