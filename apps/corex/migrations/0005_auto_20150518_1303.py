# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0004_auto_20150515_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='contracting_auth',
            field=models.CharField(max_length=255, verbose_name=b'Authority', blank=True),
        ),
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='desc',
            field=models.CharField(max_length=255, verbose_name=b'Description', blank=True),
        ),
    ]
