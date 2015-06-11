# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0012_auto_20150601_0531'),
        ('usa', '0020_fedirsexemptorg'),
    ]

    operations = [
        migrations.CreateModel(
            name='FedToxicsFacility',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('accuracy_value', models.CharField(max_length=255, null=True)),
                ('census_block_code', models.CharField(max_length=255, null=True)),
                ('city_name', models.CharField(max_length=255, null=True, verbose_name=b'City')),
                ('collect_desc', models.CharField(max_length=255, null=True)),
                ('congressional_dist_num', models.CharField(max_length=255, null=True, verbose_name=b'')),
                ('conveyor', models.CharField(max_length=255, null=True)),
                ('country_name', models.CharField(max_length=255, null=True, verbose_name=b'Country')),
                ('county_name', models.CharField(max_length=255, null=True, verbose_name=b'County')),
                ('create_date', models.CharField(max_length=255, null=True, verbose_name=b'Creation Date')),
                ('epa_region_code', models.CharField(max_length=255, null=True, verbose_name=b'EPA Region Code')),
                ('federal_agency_name', models.CharField(max_length=255, null=True, verbose_name=b'Agency')),
                ('federal_facility_code', models.CharField(max_length=255, null=True, verbose_name=b'Facility Code')),
                ('fips_code', models.CharField(max_length=255, null=True, verbose_name=b'FIPS Code')),
                ('frs_facility_detail_report_url', models.CharField(max_length=255, null=True, verbose_name=b'Report URL')),
                ('hdatum_desc', models.CharField(max_length=255, null=True)),
                ('huc_code', models.CharField(max_length=255, null=True, verbose_name=b'HUC Code')),
                ('interest_types', models.CharField(max_length=255, null=True)),
                ('latitude83', models.CharField(max_length=255, null=True)),
                ('location_address', models.CharField(max_length=255, null=True, verbose_name=b'Location')),
                ('location_description', models.CharField(max_length=255, null=True)),
                ('longitude83', models.CharField(max_length=255, null=True)),
                ('naics_code_descriptions', models.CharField(max_length=255, null=True)),
                ('naics_codes', models.CharField(max_length=255, null=True)),
                ('pgm_sys_acrnms', models.CharField(max_length=255, null=True)),
                ('postal_code', models.CharField(max_length=255, null=True)),
                ('primary_name', models.CharField(max_length=255, null=True, verbose_name=b'Primary Name')),
                ('ref_point_desc', models.CharField(max_length=255, null=True)),
                ('registry_id', models.CharField(max_length=255, null=True, verbose_name=b'Registry ID')),
                ('sic_code_descriptions', models.CharField(max_length=255, null=True)),
                ('sic_codes', models.CharField(max_length=255, null=True)),
                ('site_type_name', models.CharField(max_length=255, null=True)),
                ('source_desc', models.CharField(max_length=255, null=True)),
                ('state_code', models.CharField(max_length=255, null=True)),
                ('state_name', models.CharField(max_length=255, null=True, verbose_name=b'State')),
                ('supplemental_location', models.CharField(max_length=255, null=True)),
                ('tribal_land_code', models.CharField(max_length=255, null=True)),
                ('tribal_land_name', models.CharField(max_length=255, null=True, verbose_name=b'Tribal Land Name')),
                ('update_date', models.CharField(max_length=255, null=True, verbose_name=b'Update Date')),
                ('us_mexico_border_ind', models.CharField(max_length=255, null=True)),
            ],
            bases=('corex.basemodel',),
        ),
    ]
