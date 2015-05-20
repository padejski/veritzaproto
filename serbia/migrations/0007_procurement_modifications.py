# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0006_auto_20150520_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='procurement',
            name='modifications',
            field=models.CharField(max_length=255, verbose_name=b'Modifications', blank=True),
        ),
    ]
