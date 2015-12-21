# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0012_fedsecfiling_former_conformed_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fedsecfiling',
            name='date_of_name_change',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
