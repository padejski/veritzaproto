# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0027_auto_20150616_1254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fedcandidate',
            options={'verbose_name_plural': 'Election Candidates'},
        ),
        migrations.AddField(
            model_name='fedcandidate',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
