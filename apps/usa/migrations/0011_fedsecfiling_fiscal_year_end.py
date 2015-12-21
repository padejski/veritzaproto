# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0010_fedsecfiling_state_of_incorporation'),
    ]

    operations = [
        migrations.AddField(
            model_name='fedsecfiling',
            name='fiscal_year_end',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
