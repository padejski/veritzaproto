# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0016_auto_20160118_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companybasemodel',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='companybasemodel',
            name='alt_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='companybasemodel',
            name='alt_name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'alternative name'),
        ),
        migrations.AlterField(
            model_name='companybasemodel',
            name='directors',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='companybasemodel',
            name='duns_num',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='companybasemodel',
            name='founders',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='companybasemodel',
            name='industry',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='companybasemodel',
            name='other',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='companybasemodel',
            name='reg_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='companybasemodel',
            name='status',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='companybasemodel',
            name='type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='companybasemodel',
            name='url',
            field=models.URLField(max_length=255, null=True),
        ),
    ]
