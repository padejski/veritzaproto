# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companybasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.CompanyBaseModel')),
                ('area', models.CharField(max_length=255)),
                ('company_id', models.CharField(max_length=255)),
                ('form', models.CharField(max_length=255)),
                ('founder_number', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('tax_number', models.CharField(max_length=255)),
                ('termination_date', models.CharField(max_length=255)),
            ],
            bases=('corex.companybasemodel',),
        ),
        migrations.CreateModel(
            name='FixedAsset',
            fields=[
                ('officialmovable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.OfficialMovable')),
                ('acquisition_basis', models.CharField(max_length=255)),
                ('ownership_stake', models.CharField(max_length=255)),
                ('type_size', models.CharField(max_length=255)),
            ],
            bases=('corex.officialmovable',),
        ),
        migrations.CreateModel(
            name='Official',
            fields=[
                ('officialbasemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.OfficialBaseModel')),
                ('deposits_savings', models.NullBooleanField()),
                ('place', models.CharField(max_length=255, blank=True)),
                ('date', models.DateField(max_length=255, null=True)),
            ],
            bases=('corex.officialbasemodel',),
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('officialrealestate_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.OfficialRealEstate')),
                ('place', models.CharField(max_length=255)),
                ('structure', models.CharField(max_length=255)),
                ('allocation_basis', models.CharField(max_length=255)),
                ('closing_date', models.CharField(max_length=255)),
            ],
            bases=('corex.officialrealestate',),
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('officialsalary_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.OfficialSalary')),
                ('authority', models.CharField(max_length=255)),
                ('currency', models.CharField(max_length=255)),
                ('income_source', models.CharField(max_length=255)),
                ('interval', models.CharField(max_length=255)),
                ('net_income', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('time_period', models.CharField(max_length=255)),
            ],
            bases=('corex.officialsalary',),
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('officialmovable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.OfficialMovable')),
                ('acquisition_basis', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
            ],
            bases=('corex.officialmovable',),
        ),
    ]
