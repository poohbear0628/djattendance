# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_weekschedule_silenced_exceptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='workers_required',
        ),
    ]
