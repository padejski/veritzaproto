# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usa', '0003_fedfinancialdisclosure'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fedfinancialdisclosure',
            old_name='pdf_link',
            new_name='pdf',
        ),
    ]
