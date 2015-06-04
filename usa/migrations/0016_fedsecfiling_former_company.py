# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0015_auto_20150604_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='fedsecfiling',
            name='former_company',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
