# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150413_1909'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set([('user', 'dataset')]),
        ),
    ]
