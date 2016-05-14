# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biblereading',
            old_name='booksRead',
            new_name='books_read',
        ),
        migrations.RenameField(
            model_name='biblereading',
            old_name='weeklyReadingStatus',
            new_name='weekly_reading_status',
        ),
    ]
