# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0002_auto_20150413_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataset', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='subscriptions',
        ),
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
