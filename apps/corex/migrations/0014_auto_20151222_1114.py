# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0013_scrapetracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapetracker',
            name='last_run',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
