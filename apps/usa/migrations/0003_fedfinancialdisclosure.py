# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('usa', '0002_auto_20150518_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedFinancialDisclosure',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('filing', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('office', models.CharField(max_length=255)),
                ('pdf_link', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
            ],
            bases=('corex.basemodel',),
        ),
    ]
