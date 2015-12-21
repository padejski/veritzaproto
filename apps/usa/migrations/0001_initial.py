# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0003_auto_20150515_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedCompany',
            fields=[
                ('companybasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.CompanyBaseModel')),
                ('place', models.CharField(max_length=255)),
            ],
            bases=('corex.companybasemodel',),
        ),
        migrations.CreateModel(
            name='FedProcurement',
            fields=[
                ('procurementbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.ProcurementBaseModel')),
            ],
            bases=('corex.procurementbasemodel',),
        ),
    ]
