# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_auto_20150618_0828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='initiative',
            options={'verbose_name_plural': 'AD Initiatives', 'verbose_name': 'AD Initiative'},
        ),
    ]
