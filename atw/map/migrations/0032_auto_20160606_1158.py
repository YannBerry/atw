# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-06 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0031_trip_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripstage',
            name='massif',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='map.Massif', verbose_name='Massif'),
        ),
    ]
