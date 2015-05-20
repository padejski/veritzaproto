# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0009_auto_20150520_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procurement',
            name='contracting_auth_place',
        ),
    ]
