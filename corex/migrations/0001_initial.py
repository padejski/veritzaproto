# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import corex.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('hash', models.CharField(unique=True, max_length=255)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyBaseModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('name', models.CharField(max_length=255)),
                ('alt_name', models.CharField(max_length=255, verbose_name=b'name', blank=True)),
                ('founders', models.CharField(max_length=255, blank=True)),
                ('directors', models.CharField(max_length=255, blank=True)),
                ('type', models.CharField(max_length=255, blank=True)),
                ('industry', models.CharField(max_length=255, blank=True)),
                ('address', models.CharField(max_length=255, blank=True)),
                ('alt_address', models.CharField(max_length=255, blank=True)),
                ('registration_date', models.CharField(max_length=255, blank=True)),
                ('status', models.CharField(max_length=255, blank=True)),
                ('duns_num', models.CharField(max_length=255, blank=True)),
                ('other', models.CharField(max_length=255, blank=True)),
                ('url', models.CharField(max_length=255, blank=True)),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.CreateModel(
            name='OfficialBaseModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('year', models.CharField(max_length=255, blank=True)),
                ('other', models.CharField(max_length=255, blank=True)),
                ('url', models.CharField(max_length=255, blank=True)),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.CreateModel(
            name='OfficialChild',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('name', models.CharField(max_length=255, blank=True)),
                ('job', models.CharField(max_length=255, blank=True)),
                ('salary', models.CharField(max_length=255, blank=True)),
                ('real_estate', models.CharField(max_length=255, blank=True)),
                ('movables', models.CharField(max_length=255, blank=True)),
                ('companies', models.CharField(max_length=255, blank=True)),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.CreateModel(
            name='OfficialMovable',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.CreateModel(
            name='OfficialRealEstate',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.CreateModel(
            name='OfficialSalary',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.CreateModel(
            name='OfficialSpouse',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='corex.BaseModel')),
                ('name', models.CharField(max_length=255, blank=True)),
            ],
            bases=('corex.basemodel',),
        ),
        migrations.AddField(
            model_name='officialbasemodel',
            name='children',
            field=corex.models.UnsavedManyToManyField(to='corex.OfficialChild'),
        ),
        migrations.AddField(
            model_name='officialbasemodel',
            name='companies',
            field=corex.models.UnsavedManyToManyField(to='corex.CompanyBaseModel'),
        ),
        migrations.AddField(
            model_name='officialbasemodel',
            name='movables',
            field=corex.models.UnsavedManyToManyField(to='corex.OfficialMovable'),
        ),
        migrations.AddField(
            model_name='officialbasemodel',
            name='real_estates',
            field=corex.models.UnsavedManyToManyField(to='corex.OfficialRealEstate'),
        ),
        migrations.AddField(
            model_name='officialbasemodel',
            name='salaries',
            field=corex.models.UnsavedManyToManyField(to='corex.OfficialSalary'),
        ),
        migrations.AddField(
            model_name='officialbasemodel',
            name='spouse',
            field=corex.models.UnsavedForeignKey(to='corex.OfficialSpouse', null=True),
        ),
    ]
