# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('serbia', '0012_auto_20150715_0101'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficialCompany',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('company', models.ForeignKey(to='serbia.Company')),
                ('official', models.ForeignKey(to='serbia.Official')),
            ],
            options={
                'verbose_name': "Public Offcial's company",
                'verbose_name_plural': 'Public Officials Companies',
            },
            bases=('corex.basemodel',),
        ),
    ]
