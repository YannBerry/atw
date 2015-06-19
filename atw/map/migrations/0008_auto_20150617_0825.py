# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_auto_20150617_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative',
            name='nbr_installations',
            field=models.IntegerField(null=True, blank=True, verbose_name='Number of Installations', validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
