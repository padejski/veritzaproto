# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0025_fedcpscrecallviolation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='consumer_contact',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Consumer Contact'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='mfcs',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Manufacturers'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='action_requested',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Action Requested'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='address_1',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Address'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='foreign_mfg',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Foreign Manufacturing'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='loa_date',
            field=models.CharField(max_length=255, null=True, verbose_name=b'LOA Date'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='lot_size',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Lot Size'),
        ),
        migrations.AlterField(
            model_name='fedcpscrecallviolation',
            name='primary_violation',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Primary Violation'),
        ),
        migrations.AlterField(
            model_name='fedoshainspection',
            name='owner_code',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Owner Code'),
        ),
    ]
