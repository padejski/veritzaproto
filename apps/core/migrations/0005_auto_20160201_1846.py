# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150413_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electionscontributions',
            name='csv_file',
            field=models.FileField(null=True, upload_to=b'/home/huey/Projects/veritzaproto/media', blank=True),
        ),
    ]
