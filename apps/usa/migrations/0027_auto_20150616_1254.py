# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('usa', '0026_auto_20150612_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedElectionContribution',
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
                ('url', models.CharField(max_length=255, null=True)),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.RemoveField(
            model_name='fedcommitteecontribution',
            name='basemodel_ptr',
        ),
        migrations.RemoveField(
            model_name='fedindividualcontribution',
            name='basemodel_ptr',
        ),
        migrations.AddField(
            model_name='fedcpscrecallviolation',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fedfinancialdisclosure',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fedirsexemptorg',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fedoshaebsa',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fedoshainspection',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fedtoxicsfacility',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='FedCommitteeContribution',
        ),
        migrations.DeleteModel(
            name='FedIndividualContribution',
        ),
    ]
