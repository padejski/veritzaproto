# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0014_fedsecfiling_former_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fedsecfiling',
            old_name='former_company',
            new_name='url',
        ),
    ]
