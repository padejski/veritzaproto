# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0011_fedsecfiling_fiscal_year_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='fedsecfiling',
            name='former_conformed_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
