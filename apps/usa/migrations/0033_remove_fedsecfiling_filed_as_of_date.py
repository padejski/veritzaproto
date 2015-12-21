# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0032_auto_20150716_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fedsecfiling',
            name='filed_as_of_date',
        ),
    ]
