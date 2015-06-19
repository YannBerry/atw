# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20150610_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative',
            name='power',
            field=models.IntegerField(verbose_name='Total Power (kW)', blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
