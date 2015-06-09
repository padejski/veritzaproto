# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('usa', '0019_fedcommitteecontribution'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedIrsExemptOrg',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('city', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('ein', models.CharField(max_length=255, null=True, verbose_name=b'EIN')),
                ('name', models.CharField(max_length=255, null=True, verbose_name=b'Legal Name')),
                ('state', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(max_length=255, null=True, verbose_name=b'Deductibility Status')),
            ],
            bases=('corex.basemodel',),
        ),
    ]
