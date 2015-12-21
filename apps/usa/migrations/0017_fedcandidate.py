# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('usa', '0016_fedsecfiling_former_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedCandidate',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('cand_id', models.CharField(max_length=255, null=True)),
                ('cand_name', models.CharField(max_length=255, null=True)),
                ('cand_pty_affiliation', models.CharField(max_length=255, null=True)),
                ('cand_election_yr', models.CharField(max_length=255, null=True)),
                ('cand_office_st', models.CharField(max_length=255, null=True)),
                ('cand_office', models.CharField(max_length=255, null=True)),
                ('cand_office_district', models.CharField(max_length=255, null=True)),
                ('cand_ici', models.CharField(max_length=255, null=True)),
                ('cand_status', models.CharField(max_length=255, null=True)),
                ('cand_pcc', models.CharField(max_length=255, null=True)),
                ('cand_st1', models.CharField(max_length=255, null=True)),
                ('cand_st2', models.CharField(max_length=255, null=True)),
                ('cand_city', models.CharField(max_length=255, null=True)),
                ('cand_st', models.CharField(max_length=255, null=True)),
                ('cand_zip', models.CharField(max_length=255, null=True)),
            ],
            bases=('corex.basemodel',),
        ),
    ]
