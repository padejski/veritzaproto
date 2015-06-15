# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('usa', '0024_auto_20150611_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedCpscRecallViolation',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('action_requested', models.CharField(max_length=255, null=True)),
                ('address_1', models.CharField(max_length=255, null=True)),
                ('address_2', models.CharField(max_length=255, null=True)),
                ('citation', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('firm', models.CharField(max_length=255, null=True)),
                ('foreign_mfg', models.CharField(max_length=255, null=True)),
                ('loa_date', models.CharField(max_length=255, null=True)),
                ('lot_size', models.CharField(max_length=255, null=True)),
                ('model', models.CharField(max_length=255, null=True)),
                ('primary_violation', models.CharField(max_length=255, null=True)),
                ('product', models.CharField(max_length=255, null=True)),
            ],
            bases=('corex.basemodel',),
        ),
    ]
