# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corex', '0010_auto_20150520_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionDonationBaseModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('date', models.CharField(max_length=255, null=True)),
                ('donor_name', models.CharField(max_length=255, null=True)),
                ('donor_address', models.CharField(max_length=255, null=True)),
                ('donor_type', models.CharField(max_length=255, null=True)),
                ('other_donor', models.CharField(max_length=255, null=True)),
                ('candidate', models.CharField(max_length=255, null=True)),
                ('political_party', models.CharField(max_length=255, null=True)),
                ('election_type', models.CharField(max_length=255, null=True)),
                ('amount', models.CharField(max_length=255, null=True)),
                ('other', models.CharField(max_length=255, null=True)),
                ('url', models.CharField(max_length=255, null=True)),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='contact_person',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='contracting_auth',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Contracting Authority'),
        ),
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='desc',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Description'),
        ),
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='other',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='place',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='price',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='transaction_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='url',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='procurementbasemodel',
            name='year',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
