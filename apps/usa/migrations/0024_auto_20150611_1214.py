# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0023_fedcpscrecall_fedoshainspection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fedcpscrecall',
            old_name='description',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='fedcpscrecall',
            old_name='in_conjunctions',
            new_name='in_conj',
        ),
        migrations.RenameField(
            model_name='fedcpscrecall',
            old_name='last_publish_date',
            new_name='last_pub_date',
        ),
        migrations.RenameField(
            model_name='fedcpscrecall',
            old_name='manufacturer_countries',
            new_name='mfcs',
        ),
        migrations.RenameField(
            model_name='fedcpscrecall',
            old_name='manufacturers',
            new_name='mfcs_countries',
        ),
    ]
