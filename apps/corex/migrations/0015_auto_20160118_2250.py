# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0014_auto_20151222_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='hash',
            field=models.CharField(unique=True, max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='companybasemodel',
            name='alt_name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'alternative name'),
        ),
    ]
