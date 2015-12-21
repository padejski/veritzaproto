# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0007_procurement_modifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procurement',
            name='contracting_name',
        ),
        migrations.AddField(
            model_name='procurement',
            name='contracting_id',
            field=models.CharField(max_length=255, verbose_name=b'Contracting Authority ID', blank=True),
        ),
    ]
