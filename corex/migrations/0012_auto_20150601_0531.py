# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0011_auto_20150601_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electiondonationbasemodel',
            name='donor_address',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Donor Address'),
        ),
        migrations.AlterField(
            model_name='electiondonationbasemodel',
            name='donor_name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Donor Name'),
        ),
        migrations.AlterField(
            model_name='electiondonationbasemodel',
            name='donor_type',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Donor Type'),
        ),
        migrations.AlterField(
            model_name='electiondonationbasemodel',
            name='election_type',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Election Type'),
        ),
        migrations.AlterField(
            model_name='electiondonationbasemodel',
            name='other_donor',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Other Donor'),
        ),
        migrations.AlterField(
            model_name='electiondonationbasemodel',
            name='political_party',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Political Party'),
        ),
    ]
