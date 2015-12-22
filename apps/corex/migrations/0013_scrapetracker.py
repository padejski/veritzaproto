# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapeTracker',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('last_run', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('status', models.CharField(default=b'pending', max_length=50)),
            ],
        ),
    ]
