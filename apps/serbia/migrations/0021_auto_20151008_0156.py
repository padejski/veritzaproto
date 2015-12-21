# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0020_auto_20151007_0501'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='officialcompany',
            unique_together=set([('official', 'company')]),
        ),
    ]
