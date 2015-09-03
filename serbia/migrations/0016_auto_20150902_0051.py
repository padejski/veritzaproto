# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0015_politicalfundercompany'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='legal_rep',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='members',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='other_individuals',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='supervisors',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
