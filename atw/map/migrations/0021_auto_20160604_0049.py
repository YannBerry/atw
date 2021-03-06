# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-03 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0020_auto_20160603_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='initiative',
            name='need',
        ),
        migrations.RemoveField(
            model_name='initiative',
            name='stage',
        ),
        migrations.RemoveField(
            model_name='initiative',
            name='status',
        ),
        migrations.AlterModelOptions(
            name='tripstage',
            options={'ordering': ['date'], 'verbose_name': 'Stage', 'verbose_name_plural': 'Stages'},
        ),
        migrations.RemoveField(
            model_name='trip',
            name='stage_name',
        ),
        migrations.AddField(
            model_name='trip',
            name='stages',
            field=models.ManyToManyField(to='map.TripStage', verbose_name='Stages'),
        ),
        migrations.DeleteModel(
            name='Initiative',
        ),
        migrations.DeleteModel(
            name='Need',
        ),
        migrations.DeleteModel(
            name='Stage',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
