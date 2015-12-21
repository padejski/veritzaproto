# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0006_fedsecfiling_date_as_of_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='fedsecfiling',
            name='irs_number',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
