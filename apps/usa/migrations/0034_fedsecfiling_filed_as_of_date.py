# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0033_remove_fedsecfiling_filed_as_of_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='fedsecfiling',
            name='filed_as_of_date',
            field=models.DateField(null=True, verbose_name=b'Filing` Date'),
        ),
    ]
