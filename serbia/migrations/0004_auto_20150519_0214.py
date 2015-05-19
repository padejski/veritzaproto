# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import corex.models


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0003_auto_20150519_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='officials',
            field=corex.models.UnsavedManyToManyField(to='serbia.Official'),
        ),
        migrations.AddField(
            model_name='realestate',
            name='official',
            field=corex.models.UnsavedForeignKey(to='serbia.Official', null=True),
        ),
        migrations.AddField(
            model_name='salary',
            name='official',
            field=corex.models.UnsavedForeignKey(to='serbia.Official', null=True),
        ),
    ]
