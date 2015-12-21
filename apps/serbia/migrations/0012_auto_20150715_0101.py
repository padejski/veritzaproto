# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0011_auto_20150601_0302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='electiondonation',
            options={'verbose_name_plural': 'Election Contributions'},
        ),
        migrations.RemoveField(
            model_name='company',
            name='form',
        ),
    ]
