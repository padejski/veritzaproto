# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('usa', '0022_fedoshaebsa'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedCpscRecall',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('consumer_contact', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('hazards', models.CharField(max_length=255, null=True)),
                ('images', models.CharField(max_length=255, null=True)),
                ('in_conjunctions', models.CharField(max_length=255, null=True)),
                ('injuries', models.CharField(max_length=255, null=True)),
                ('last_publish_date', models.CharField(max_length=255, null=True)),
                ('manufacturer_countries', models.CharField(max_length=255, null=True)),
                ('manufacturers', models.CharField(max_length=255, null=True)),
                ('products', models.CharField(max_length=255, null=True)),
                ('product_upcs', models.CharField(max_length=255, null=True)),
                ('recall_date', models.CharField(max_length=255, null=True)),
                ('recall_id', models.CharField(max_length=255, null=True)),
                ('recall_num', models.CharField(max_length=255, null=True)),
                ('remedies', models.CharField(max_length=255, null=True)),
                ('retailers', models.CharField(max_length=255, null=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('url', models.CharField(max_length=255, null=True)),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.CreateModel(
            name='FedOshaInspection',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('activity_nr', models.CharField(max_length=255, null=True, verbose_name=b'Inspection ID')),
                ('adv_notice', models.CharField(max_length=255, null=True, verbose_name=b'Advance Notice')),
                ('case_mod_date', models.CharField(max_length=255, null=True)),
                ('close_case_date', models.CharField(max_length=255, null=True)),
                ('close_conf_date', models.CharField(max_length=255, null=True)),
                ('estab_name', models.CharField(max_length=255, null=True, verbose_name=b'Establishment Name')),
                ('health_const', models.CharField(max_length=255, null=True)),
                ('health_manuf', models.CharField(max_length=255, null=True)),
                ('health_marit', models.CharField(max_length=255, null=True)),
                ('host_est_key', models.CharField(max_length=255, null=True)),
                ('indstry_dim_id', models.CharField(max_length=255, null=True)),
                ('insp_scope', models.CharField(max_length=255, null=True)),
                ('insp_type', models.CharField(max_length=255, null=True)),
                ('ld_dt', models.CharField(max_length=255, null=True)),
                ('mail_city', models.CharField(max_length=255, null=True)),
                ('mail_state', models.CharField(max_length=255, null=True)),
                ('mail_street', models.CharField(max_length=255, null=True)),
                ('mail_zip', models.CharField(max_length=255, null=True)),
                ('migrant', models.CharField(max_length=255, null=True)),
                ('naics_code', models.CharField(max_length=255, null=True, verbose_name=b'NAICS Code')),
                ('nr_in_estab', models.CharField(max_length=255, null=True)),
                ('open_date', models.CharField(max_length=255, null=True)),
                ('owner_code', models.CharField(max_length=255, null=True)),
                ('owner_type', models.CharField(max_length=255, null=True)),
                ('reporting_id', models.CharField(max_length=255, null=True)),
                ('safety_const', models.CharField(max_length=255, null=True)),
                ('safety_hlth', models.CharField(max_length=255, null=True)),
                ('safety_manuf', models.CharField(max_length=255, null=True)),
                ('safety_marit', models.CharField(max_length=255, null=True)),
                ('sic_code', models.CharField(max_length=255, null=True)),
                ('site_address', models.CharField(max_length=255, null=True)),
                ('site_city', models.CharField(max_length=255, null=True, verbose_name=b'City')),
                ('site_state', models.CharField(max_length=255, null=True, verbose_name=b'State')),
                ('site_zip', models.CharField(max_length=255, null=True, verbose_name=b'ZIP')),
                ('state_flag', models.CharField(max_length=255, null=True)),
                ('union_status', models.CharField(max_length=255, null=True)),
                ('why_no_insp', models.CharField(max_length=255, null=True, verbose_name=b'No Inspection Reason')),
                ('zip_dim_id', models.CharField(max_length=255, null=True)),
            ],
            bases=('corex.basemodel',),
        ),
    ]
