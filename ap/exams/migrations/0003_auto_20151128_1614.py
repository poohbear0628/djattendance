# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.contrib.postgres.fields.hstore


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150905_1512'),
        ('exams', '0002_exam_examinstance_response_retake_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('responses', django.contrib.postgres.fields.hstore.HStoreField(null=True)),
                ('score', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_submitted_online', models.BooleanField(default=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('is_graded', models.BooleanField(default=False)),
                ('retake_number', models.IntegerField(default=0)),
                ('grade', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='examinstance',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='examinstance',
            name='trainee',
        ),
        migrations.RemoveField(
            model_name='response',
            name='instance',
        ),
        migrations.RemoveField(
            model_name='response',
            name='trainee',
        ),
        migrations.RenameField(
            model_name='retake',
            old_name='exam_template',
            new_name='exam',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='is_midterm',
        ),
        migrations.AddField(
            model_name='exam',
            name='category',
            field=models.CharField(default='M', max_length=1, choices=[(b'M', b'Midterm'), (b'F', b'Final')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0, 5400)),
        ),
        migrations.AddField(
            model_name='exam',
            name='name',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='section',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='ExamInstance',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
        migrations.AddField(
            model_name='session',
            name='exam',
            field=models.ForeignKey(to='exams.Exam'),
        ),
        migrations.AddField(
            model_name='session',
            name='trainee',
            field=models.ForeignKey(to='accounts.Trainee'),
        ),
        migrations.AddField(
            model_name='responses',
            name='instance',
            field=models.ForeignKey(to='exams.Session'),
        ),
        migrations.AddField(
            model_name='responses',
            name='section',
            field=models.ForeignKey(to='exams.Section'),
        ),
        migrations.AddField(
            model_name='responses',
            name='trainee',
            field=models.ForeignKey(to='accounts.Trainee'),
        ),
    ]
