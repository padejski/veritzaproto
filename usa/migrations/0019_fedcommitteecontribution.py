# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('usa', '0018_auto_20150605_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedCommitteeContribution',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('amndt_ind', models.CharField(max_length=255, null=True, verbose_name=b'Amendment')),
                ('cand_id', models.CharField(max_length=255, null=True, verbose_name=b'Candidate')),
                ('city', models.CharField(max_length=255, null=True)),
                ('cmte_id', models.CharField(max_length=255, null=True, verbose_name=b'Committee ID')),
                ('employer', models.CharField(max_length=255, null=True)),
                ('entity_tp', models.CharField(max_length=255, null=True, verbose_name=b'Entity Type')),
                ('file_num', models.CharField(max_length=255, null=True, verbose_name=b'File Number')),
                ('image_num', models.CharField(max_length=255, null=True, verbose_name=b'Microfilm Location')),
                ('memo_cd', models.CharField(max_length=255, null=True, verbose_name=b'Memo Code')),
                ('memo_text', models.CharField(max_length=255, null=True, verbose_name=b'Memo Text')),
                ('name', models.CharField(max_length=255, null=True, verbose_name=b'Contributor Name')),
                ('occupation', models.CharField(max_length=255, null=True)),
                ('other_id', models.CharField(max_length=255, null=True, verbose_name=b'Other ID')),
                ('rpt_tp', models.CharField(max_length=255, null=True, verbose_name=b'Report Type')),
                ('state', models.CharField(max_length=255, null=True)),
                ('sub_id', models.CharField(max_length=255, null=True, verbose_name=b'FEC Record Number')),
                ('tran_id', models.CharField(max_length=255, null=True, verbose_name=b'Transaction ID')),
                ('transaction_amt', models.CharField(max_length=255, null=True, verbose_name=b'Transaction Amount')),
                ('transaction_dt', models.CharField(max_length=255, null=True, verbose_name=b'Transaction Date')),
                ('transaction_pgi', models.CharField(max_length=255, null=True, verbose_name=b'Primary-Gen Indicator')),
                ('transaction_tp', models.CharField(max_length=255, null=True, verbose_name=b'Transaction Type')),
                ('zip_code', models.CharField(max_length=255, null=True, verbose_name=b'Zip Code')),
            ],
            bases=('corex.basemodel',),
        ),
    ]
