# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fedcompany',
            options={'verbose_name_plural': 'Federal Companies'},
        ),
        migrations.AlterModelOptions(
            name='fedprocurement',
            options={'verbose_name_plural': 'Procurements'},
        ),
    ]
