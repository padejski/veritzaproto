# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('serbia', '0016_auto_20150902_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPoliticalFunderProcurement',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('company', models.ForeignKey(to='serbia.Company')),
                ('procurement', models.ForeignKey(to='serbia.Procurement')),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.CreateModel(
            name='PoliticalFunderCompanyProcurement',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('company', models.ForeignKey(to='serbia.PoliticalFunderCompany')),
                ('procurement', models.ForeignKey(to='serbia.Procurement')),
            ],
            bases=('corex.basemodel',),
        ),
    ]
