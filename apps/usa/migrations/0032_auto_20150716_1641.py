# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0031_auto_20150707_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fedcpscrecall',
            options={'verbose_name_plural': 'Consumer Product Safety Commission Recalls'},
        ),
        migrations.AlterModelOptions(
            name='fedcpscrecallviolation',
            options={'verbose_name_plural': 'Consumer Product Safety Commission Recall Violations'},
        ),
        migrations.AlterModelOptions(
            name='fedelectioncontribution',
            options={'verbose_name_plural': 'Elections Contributions'},
        ),
        migrations.AlterModelOptions(
            name='fedfinancialdisclosure',
            options={'verbose_name_plural': 'Federal Financial Disclosures'},
        ),
        migrations.AlterModelOptions(
            name='fedirsexemptorg',
            options={'verbose_name_plural': 'IRS Exempt Organizations'},
        ),
        migrations.AlterModelOptions(
            name='fedoshaebsa',
            options={'verbose_name_plural': 'OSHA Employees Benefits Security Adminstration Enforcements'},
        ),
        migrations.AlterModelOptions(
            name='fedoshainspection',
            options={'verbose_name_plural': 'Occupational Safety and Health Inspections'},
        ),
        migrations.AlterModelOptions(
            name='fedprocurement',
            options={'verbose_name_plural': 'Federal Procurements'},
        ),
        migrations.AlterModelOptions(
            name='fedsecfiling',
            options={'verbose_name_plural': 'Securities and Exchange Commission Filings'},
        ),
        migrations.AlterModelOptions(
            name='fedtoxicsfacility',
            options={'verbose_name_plural': 'Toxics Facilities'},
        ),
        migrations.AlterField(
            model_name='fedcpscrecall',
            name='title',
            field=models.CharField(max_length=1024, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='company_conformed_name',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Company Name'),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='irs_number',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'IRS Number'),
        ),
        migrations.AlterField(
            model_name='fedsecfiling',
            name='sec_file_number',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'SEC File Number'),
        ),
    ]
