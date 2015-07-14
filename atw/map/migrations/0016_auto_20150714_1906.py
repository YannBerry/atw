# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0015_auto_20150708_1957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stage',
            options={'verbose_name_plural': 'Stages', 'verbose_name': 'Stage', 'ordering': ['stage']},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Status', 'verbose_name': 'Status', 'ordering': ['status']},
        ),
        migrations.AlterField(
            model_name='initiative',
            name='description',
            field=models.TextField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='stage',
            field=models.ForeignKey(to='map.Stage', verbose_name='Stage'),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='status',
            field=models.ForeignKey(to='map.Status', verbose_name='Status'),
        ),
    ]
