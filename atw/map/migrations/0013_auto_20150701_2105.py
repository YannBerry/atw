# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0012_auto_20150618_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='initiative',
            name='added_by',
            field=models.CharField(max_length=50, verbose_name='Added by', default='rate'),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(max_length=25, verbose_name='Status'),
        ),
    ]
