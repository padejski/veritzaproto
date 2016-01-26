# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.corex.models


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0021_auto_20151008_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='officials',
            field=apps.corex.models.UnsavedManyToManyField(to='serbia.Official', null=True),
        ),
    ]
