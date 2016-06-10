# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-10 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0044_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripstage',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='map.Country', verbose_name='Pays'),
            preserve_default=False,
        ),
    ]
