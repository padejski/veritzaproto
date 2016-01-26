# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.corex.models


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0022_auto_20160118_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='officials',
            field=apps.corex.models.UnsavedManyToManyField(to='serbia.Official', blank=True),
        ),
    ]
