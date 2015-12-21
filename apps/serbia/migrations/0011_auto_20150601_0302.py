# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0011_auto_20150601_0301'),
        ('serbia', '0010_remove_procurement_contracting_auth_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionDonation',
            fields=[
                ('electiondonationbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.ElectionDonationBaseModel')),
                ('donation', models.CharField(max_length=255, null=True)),
                ('dues', models.CharField(max_length=255, null=True)),
                ('kind_donations', models.CharField(max_length=255, null=True)),
                ('selection', models.CharField(max_length=255, null=True)),
            ],
            bases=('corex.electiondonationbasemodel',),
        ),
        migrations.RemoveField(
            model_name='procurement',
            name='suppliers_state',
        ),
        migrations.AlterField(
            model_name='procurement',
            name='default_reason',
            field=models.CharField(max_length=255, verbose_name=b'Reason of Failure', blank=True),
        ),
        migrations.AlterField(
            model_name='procurement',
            name='modifications',
            field=models.CharField(max_length=255, verbose_name=b'Changes', blank=True),
        ),
    ]
