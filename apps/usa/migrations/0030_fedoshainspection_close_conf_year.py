# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0029_auto_20150703_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='fedoshainspection',
            name='close_conf_year',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
