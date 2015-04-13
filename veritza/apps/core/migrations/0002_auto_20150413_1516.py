# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conflictinterest',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='conflictinterest',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 22, 16, 6, 912854, tzinfo=utc), verbose_name='Created Timestamp', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conflictinterest',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='conflictinterest',
            name='is_ok',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='conflictinterest',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 22, 16, 11, 165751, tzinfo=utc), verbose_name='Last Modified', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conflictinterest',
            name='uuid',
            field=django_extensions.db.fields.UUIDField(default='', verbose_name=uuid.uuid4, max_length=36, editable=False, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conflictinterestfamilymember',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='conflictinterestfamilymember',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 22, 16, 23, 964872, tzinfo=utc), verbose_name='Created Timestamp', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conflictinterestfamilymember',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='conflictinterestfamilymember',
            name='is_ok',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='conflictinterestfamilymember',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 22, 16, 27, 586512, tzinfo=utc), verbose_name='Last Modified', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conflictinterestfamilymember',
            name='uuid',
            field=django_extensions.db.fields.UUIDField(default='', verbose_name=uuid.uuid4, max_length=36, editable=False, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publicofficialcompany',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='publicofficialcompany',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 22, 16, 36, 864162, tzinfo=utc), verbose_name='Created Timestamp', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publicofficialcompany',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='publicofficialcompany',
            name='is_ok',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='publicofficialcompany',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 22, 16, 41, 678453, tzinfo=utc), verbose_name='Last Modified', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publicofficialcompany',
            name='uuid',
            field=django_extensions.db.fields.UUIDField(default='', verbose_name=uuid.uuid4, max_length=36, editable=False, blank=True),
            preserve_default=False,
        ),
    ]
