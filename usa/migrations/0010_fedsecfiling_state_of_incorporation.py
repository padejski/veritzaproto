# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0009_auto_20150604_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='fedsecfiling',
            name='state_of_incorporation',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
