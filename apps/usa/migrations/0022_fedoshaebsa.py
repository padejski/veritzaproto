# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('usa', '0021_fedtoxicsfacility'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedOshaEbsa',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('case_type', models.CharField(max_length=255, null=True, verbose_name=b'Case Type')),
                ('ein', models.CharField(max_length=255, null=True, verbose_name=b'EIN')),
                ('final_close_date', models.CharField(max_length=255, null=True, verbose_name=b'Closing Date')),
                ('final_close_reason', models.CharField(max_length=255, null=True, verbose_name=b'Closing Reason')),
                ('penalty_amount', models.CharField(max_length=255, null=True, verbose_name=b'Penalty Amount')),
                ('plan_admin', models.CharField(max_length=255, null=True, verbose_name=b'Administrator')),
                ('plan_admin_state', models.CharField(max_length=255, null=True, verbose_name=b'Admin State')),
                ('plan_admin_zip_code', models.CharField(max_length=255, null=True, verbose_name=b'Admin Zip Code')),
                ('plan_name', models.CharField(max_length=255, null=True, verbose_name=b'Plan Name')),
                ('plan_year', models.CharField(max_length=255, null=True, verbose_name=b'Plan Year')),
                ('pn', models.CharField(max_length=255, null=True, verbose_name=b'Plan Number')),
            ],
            bases=('corex.basemodel',),
        ),
    ]
