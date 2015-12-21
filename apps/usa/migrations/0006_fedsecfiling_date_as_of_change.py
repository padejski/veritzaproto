# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0005_fedsecfiling'),
    ]

    operations = [
        migrations.AddField(
            model_name='fedsecfiling',
            name='date_as_of_change',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
