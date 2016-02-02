# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0017_auto_20160119_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companybasemodel',
            name='alt_name',
            field=models.CharField(default='err', max_length=255, verbose_name=b'alternative name', blank=True),
            preserve_default=False,
        ),
    ]
