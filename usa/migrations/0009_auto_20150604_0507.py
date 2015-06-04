# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0008_fedsecfiling_street_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='fedsecfiling',
            name='business_phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fedsecfiling',
            name='mail_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fedsecfiling',
            name='standard_industrial_classification',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='accession_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='business_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='central_index_key',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='company_conformed_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='company_data',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='conformed_submission_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='filed_as_of_date',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='filer',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='filing_values',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='film_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='form_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='public_document_count',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='sec_act',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='sec_file_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='state',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='street_1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='zip',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
