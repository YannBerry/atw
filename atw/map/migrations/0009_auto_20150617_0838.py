# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_auto_20150617_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative',
            name='nbr_installations',
            field=models.IntegerField(null=True, blank=True, verbose_name='Number of Installations'),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='power',
            field=models.IntegerField(null=True, blank=True, verbose_name='Total Power (kW)'),
        ),
    ]
