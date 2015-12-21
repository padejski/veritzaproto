# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0008_auto_20150520_0753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='procurement',
            old_name='contracting_id',
            new_name='contracting_auth_id',
        ),
    ]
