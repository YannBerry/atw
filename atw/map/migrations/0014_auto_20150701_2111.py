# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0013_auto_20150701_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative',
            name='added_by',
            field=models.CharField(max_length=50, verbose_name='Added by'),
        ),
    ]
