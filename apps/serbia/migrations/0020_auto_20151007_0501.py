# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0019_auto_20150910_0012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='electiondonation',
            options={'verbose_name_plural': 'Election Donations'},
        ),
        migrations.AlterModelOptions(
            name='official',
            options={'verbose_name_plural': 'Officials'},
        ),
        migrations.AlterModelOptions(
            name='procurement',
            options={'verbose_name_plural': 'Procurements'},
        ),
    ]
