# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serbia', '0005_procurement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='procurement',
            old_name='llp_basis',
            new_name='lpp_basis',
        ),
    ]
