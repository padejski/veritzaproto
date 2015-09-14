# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0017_companypoliticalfunderprocurement_politicalfundercompanyprocurement'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PoliticalFunderCompanyProcurement',
            new_name='CompanyFunderProcurement',
        ),
        migrations.RenameModel(
            old_name='PoliticalFunderCompany',
            new_name='FunderCompany',
        ),
        migrations.RenameModel(
            old_name='CompanyPoliticalFunderProcurement',
            new_name='FunderCompanyProcurement',
        ),
        migrations.AlterField(
            model_name='companyfunderprocurement',
            name='company',
            field=models.ForeignKey(to='serbia.Company'),
        ),
        migrations.AlterField(
            model_name='fundercompanyprocurement',
            name='company',
            field=models.ForeignKey(to='serbia.Company', to_field='basemodel_ptr'),
        ),
    ]
