# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0018_auto_20160201_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companybasemodel',
            name='alt_name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'alternative name', blank=True),
        ),
    ]
