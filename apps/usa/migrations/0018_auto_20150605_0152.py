# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('usa', '0017_fedcandidate'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedIndividualContribution',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('cmte_id', models.CharField(max_length=255, null=True)),
                ('amndt_ind', models.CharField(max_length=255, null=True, verbose_name=b'Amendment')),
                ('rpt_tp', models.CharField(max_length=255, null=True, verbose_name=b'Report Type')),
                ('transaction_pgi', models.CharField(max_length=255, null=True, verbose_name=b'Primary-General Indicator')),
                ('image_num', models.CharField(max_length=255, null=True, verbose_name=b'Microfilm Location')),
                ('transaction_tp', models.CharField(max_length=255, null=True, verbose_name=b'Transaction Type')),
                ('entity_tp', models.CharField(max_length=255, null=True, verbose_name=b'Entity Type')),
                ('name', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('zip_code', models.CharField(max_length=255, null=True, verbose_name=b'Zip Code')),
                ('employer', models.CharField(max_length=255, null=True)),
                ('occupation', models.CharField(max_length=255, null=True)),
                ('transaction_dt', models.CharField(max_length=255, null=True, verbose_name=b'Date')),
                ('transaction_amt', models.CharField(max_length=255, null=True, verbose_name=b'Amount')),
                ('other_id', models.CharField(max_length=255, null=True, verbose_name=b'Other ID')),
                ('tran_id', models.CharField(max_length=255, null=True, verbose_name=b'Transaction ID')),
                ('file_num', models.CharField(max_length=255, null=True, verbose_name=b'File Number')),
                ('memo_cd', models.CharField(max_length=255, null=True, verbose_name=b'Memo Code')),
                ('memo_text', models.CharField(max_length=255, null=True, verbose_name=b'Memo Text')),
                ('sub_id', models.CharField(max_length=255, null=True, verbose_name=b'FEC Record Number')),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_city',
            field=models.CharField(max_length=255, null=True, verbose_name=b'City'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_election_yr',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Election Year'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_ici',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Incumbent Challenger Status'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_office',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Office'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_office_district',
            field=models.CharField(max_length=255, null=True, verbose_name=b'District'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_office_st',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Office State'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_pcc',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Campaign Committee'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_pty_affiliation',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Party Affiliation'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_st',
            field=models.CharField(max_length=255, null=True, verbose_name=b'State'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_st1',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Street'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_st2',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Street2'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_status',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Status'),
        ),
        migrations.AlterField(
            model_name='fedcandidate',
            name='cand_zip',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Zip Code'),
        ),
    ]
