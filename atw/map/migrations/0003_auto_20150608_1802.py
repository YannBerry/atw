# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_initiative_date_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['status'], 'verbose_name_plural': 'Status'},
        ),
        migrations.AlterField(
            model_name='initiative',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='start',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Beginning of the project', blank=True),
        ),
    ]
