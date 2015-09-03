# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('serbia', '0014_auto_20150825_0319'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticalFunderCompany',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('company', models.ForeignKey(to='serbia.Company')),
                ('donation', models.ForeignKey(to='serbia.ElectionDonation')),
            ],
            bases=('corex.basemodel',),
        ),
    ]
