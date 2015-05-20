# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0009_auto_20150519_0214'),
        ('serbia', '0004_auto_20150519_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('procurementbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.ProcurementBaseModel')),
                ('contracting_auth_address', models.CharField(max_length=255, verbose_name=b'Contracting Authority Address', blank=True)),
                ('contracting_auth_place', models.CharField(max_length=255, verbose_name=b'Contracting Authority Municiplaity', blank=True)),
                ('contracting_name', models.CharField(max_length=255, verbose_name=b'Name of Contracting', blank=True)),
                ('default_reason', models.CharField(max_length=255, verbose_name=b'Reason of Default', blank=True)),
                ('orn_code', models.CharField(max_length=255, verbose_name=b'ORN Code', blank=True)),
                ('llp_basis', models.CharField(max_length=255, verbose_name=b'basis of LPP', blank=True)),
                ('ppo_reviews', models.CharField(max_length=255, verbose_name=b'PPO reviews', blank=True)),
                ('procedure_type', models.CharField(max_length=255, verbose_name=b'Procedure type', blank=True)),
                ('suppliers_state', models.CharField(max_length=255, verbose_name=b'Supplier State', blank=True)),
                ('subject', models.CharField(max_length=255, verbose_name=b'Procurement Subject', blank=True)),
                ('purchases_val_contract', models.CharField(max_length=255, verbose_name=b'Contract value of purchases', blank=True)),
                ('purchases_val_estimate', models.CharField(max_length=255, verbose_name=b'Estimate value of purchases', blank=True)),
                ('offers', models.CharField(max_length=255, verbose_name=b'Offers', blank=True)),
                ('selection_criterion', models.CharField(max_length=255, verbose_name=b'Criterion of selection', blank=True)),
                ('preparing_bids_cost', models.CharField(max_length=255, verbose_name=b'Cost of Preparing bids', blank=True)),
                ('execution_date', models.DateField(null=True, verbose_name=b'Date of execution / non-execution')),
                ('execution_value', models.CharField(max_length=255, verbose_name=b'Execution of contract value excl. VAT', blank=True)),
                ('eq_price', models.CharField(max_length=255, verbose_name=b'Eq. price', blank=True)),
                ('execution_note', models.CharField(max_length=255, verbose_name=b'Execution / non-execution note', blank=True)),
                ('cases_types', models.CharField(max_length=255, verbose_name=b'Types of cases procurement', blank=True)),
                ('supplier_name', models.CharField(max_length=255, verbose_name=b'Name of Vendor/Supplier', blank=True)),
                ('supplier_id', models.CharField(max_length=255, verbose_name=b'Vendor/Supplier ID', blank=True)),
                ('supplier_country', models.CharField(max_length=255, verbose_name=b"Vendor's Country", blank=True)),
            ],
            bases=('corex.procurementbasemodel',),
        ),
    ]
