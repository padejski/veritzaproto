# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('serbia', '0018_auto_20150909_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundingCompanyProcurement',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.RenameModel(
            old_name='CompanyFunderProcurement',
            new_name='FundingCompany',
        ),
        migrations.RemoveField(
            model_name='fundingcompany',
            name='procurement',
        ),
        migrations.AddField(
            model_name='fundingcompany',
            name='donation',
            field=models.ForeignKey(default=1, to='serbia.ElectionDonation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fundercompanyprocurement',
            name='company',
            field=models.ForeignKey(to='serbia.FunderCompany'),
        ),
        migrations.AddField(
            model_name='fundingcompanyprocurement',
            name='company',
            field=models.ForeignKey(to='serbia.FundingCompany'),
        ),
        migrations.AddField(
            model_name='fundingcompanyprocurement',
            name='procurement',
            field=models.ForeignKey(to='serbia.Procurement'),
        ),
    ]
