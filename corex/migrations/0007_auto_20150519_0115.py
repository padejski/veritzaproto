# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import corex.models


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0006_auto_20150518_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officialbasemodel',
            name='movables',
        ),
        migrations.AddField(
            model_name='officialmovable',
            name='official',
            field=corex.models.UnsavedForeignKey(to='corex.OfficialBaseModel', null=True),
        ),
    ]
