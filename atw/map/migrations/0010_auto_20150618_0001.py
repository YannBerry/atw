# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0009_auto_20150617_0838'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='initiative',
            options={'verbose_name_plural': 'AD Initiatives'},
        ),
        migrations.AlterField(
            model_name='initiative',
            name='nbr_installations',
            field=models.IntegerField(verbose_name='Number of Installations', blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='power',
            field=models.IntegerField(verbose_name='Total Power (kW)', blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
