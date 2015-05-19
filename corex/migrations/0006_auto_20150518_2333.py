# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0005_auto_20150518_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companybasemodel',
            name='url',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='officialbasemodel',
            name='url',
            field=models.URLField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='url',
            field=models.URLField(max_length=255, blank=True),
        ),
    ]
