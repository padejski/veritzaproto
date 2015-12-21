# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0013_fedsecfiling_date_of_name_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='fedsecfiling',
            name='former_company',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
