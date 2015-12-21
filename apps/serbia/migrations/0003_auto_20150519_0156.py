# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.corex.models


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0002_auto_20150518_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixedasset',
            name='official',
            field=apps.corex.models.UnsavedForeignKey(to='serbia.Official', null=True),
        ),
        migrations.AddField(
            model_name='transport',
            name='official',
            field=apps.corex.models.UnsavedForeignKey(to='serbia.Official', null=True),
        ),
    ]
