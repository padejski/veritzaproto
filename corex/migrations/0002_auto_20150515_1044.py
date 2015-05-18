# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import corex.models


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcurementBaseModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('contact_person', models.CharField(max_length=255, blank=True)),
                ('contracting_auth', models.CharField(max_length=255, blank=True)),
                ('date', models.DateField(null=True)),
                ('desc', models.CharField(max_length=255, blank=True)),
                ('year', models.CharField(max_length=255, blank=True)),
                ('place', models.CharField(max_length=255, blank=True)),
                ('price', models.CharField(max_length=255, blank=True)),
                ('transaction_id', models.CharField(max_length=255, blank=True)),
                ('type', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255, blank=True)),
                ('other', models.CharField(max_length=255, blank=True)),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.RemoveField(
            model_name='companybasemodel',
            name='registration_date',
        ),
        migrations.AddField(
            model_name='companybasemodel',
            name='reg_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='procurementbasemodel',
            name='vendor',
            field=corex.models.UnsavedForeignKey(to='corex.CompanyBaseModel', null=True),
        ),
    ]
