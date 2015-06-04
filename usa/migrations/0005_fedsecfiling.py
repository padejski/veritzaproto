# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('usa', '0004_auto_20150603_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedSecFiling',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('filer', models.CharField(max_length=255)),
                ('business_address', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
                ('central_index_key', models.CharField(max_length=255)),
                ('accession_number', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('film_number', models.CharField(max_length=255)),
                ('form_type', models.CharField(max_length=255)),
                ('filed_as_of_date', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('conformed_submission_type', models.CharField(max_length=255)),
                ('street_1', models.CharField(max_length=255)),
                ('public_document_count', models.CharField(max_length=255)),
                ('sec_act', models.CharField(max_length=255)),
                ('company_conformed_name', models.CharField(max_length=255)),
                ('company_data', models.CharField(max_length=255)),
                ('filing_values', models.CharField(max_length=255)),
                ('sec_file_number', models.CharField(max_length=255)),
            ],
            bases=('corex.basemodel',),
        ),
    ]
