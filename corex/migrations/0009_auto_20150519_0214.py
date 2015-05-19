# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0008_remove_officialmovable_official'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officialbasemodel',
            name='children',
        ),
        migrations.RemoveField(
            model_name='officialbasemodel',
            name='companies',
        ),
        migrations.RemoveField(
            model_name='officialbasemodel',
            name='real_estates',
        ),
        migrations.RemoveField(
            model_name='officialbasemodel',
            name='salaries',
        ),
        migrations.RemoveField(
            model_name='officialbasemodel',
            name='spouse',
        ),
    ]
