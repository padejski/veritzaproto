# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0007_auto_20150519_0115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officialmovable',
            name='official',
        ),
    ]
