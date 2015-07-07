# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0030_fedoshainspection_close_conf_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='fedoshainspection',
            name='case_mod_year',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='fedoshainspection',
            name='close_case_year',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='fedoshainspection',
            name='inspection_to_filter',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='fedoshainspection',
            name='open_year',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='fedoshainspection',
            name='osha_accident_indicator',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='fedoshainspection',
            name='violation_type_o',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='fedoshainspection',
            name='violation_type_r',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='fedoshainspection',
            name='violation_type_s',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='fedoshainspection',
            name='violation_type_u',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='fedoshainspection',
            name='violation_type_w',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
