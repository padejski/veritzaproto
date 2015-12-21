# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('serbia', '0013_officialcompany'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficialCompanyProcurement',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('company', models.ForeignKey(to='serbia.Company')),
                ('official', models.ForeignKey(to='serbia.Official')),
                ('procurement', models.ForeignKey(to='serbia.Procurement')),
            ],
            options={
                'verbose_name': "Public Official's Company in Procurement",
                'verbose_name_plural': 'Public Officials Companies in Procurement',
            },
            bases=('corex.basemodel',),
        ),
        migrations.AlterModelOptions(
            name='officialcompany',
            options={'verbose_name': "Public Official's company", 'verbose_name_plural': 'Public Officials Companies'},
        ),
    ]
