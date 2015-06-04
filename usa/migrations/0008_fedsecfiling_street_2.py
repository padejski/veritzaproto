# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0007_fedsecfiling_irs_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='fedsecfiling',
            name='street_2',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
