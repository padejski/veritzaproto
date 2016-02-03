# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0018_auto_20160201_1822'),
        ('usa', '0034_fedsecfiling_filed_as_of_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedFunderCompany',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('company', models.ForeignKey(to='usa.FedCompany')),
                ('contribution', models.ForeignKey(to='usa.FedElectionContribution')),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.CreateModel(
            name='FedFunderCompanyProcurement',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('company', models.ForeignKey(to='usa.FedFunderCompany')),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.CreateModel(
            name='FedFundingCompany',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('company', models.ForeignKey(to='usa.FedCompany')),
                ('donation', models.ForeignKey(to='usa.FedElectionContribution')),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.CreateModel(
            name='FedFundingCompanyProcurement',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('company', models.ForeignKey(to='usa.FedFundingCompany')),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.AlterModelOptions(
            name='fedprocurement',
            options={'verbose_name_plural': 'Federal Procurement'},
        ),
        migrations.AddField(
            model_name='fedfundingcompanyprocurement',
            name='procurement',
            field=models.ForeignKey(to='usa.FedProcurement'),
        ),
        migrations.AddField(
            model_name='fedfundercompanyprocurement',
            name='procurement',
            field=models.ForeignKey(to='usa.FedProcurement'),
        ),
    ]
