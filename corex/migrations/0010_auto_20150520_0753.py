# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0009_auto_20150519_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='contracting_auth',
            field=models.CharField(max_length=255, verbose_name=b'Contracting Authority', blank=True),
        ),
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='date',
            field=models.DateField(null=True, verbose_name=b'Contract Date'),
        ),
    ]
