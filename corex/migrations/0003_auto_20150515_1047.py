# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0002_auto_20150515_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='type',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
