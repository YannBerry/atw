# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0017_need'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='initiative',
            name='project_leader',
        ),
        migrations.AddField(
            model_name='initiative',
            name='need',
            field=models.ForeignKey(to='map.Need', default=2, verbose_name='Need'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='initiative',
            name='project_owner',
            field=models.CharField(max_length=50, default='Yann', verbose_name='Project Owner'),
            preserve_default=False,
        ),
    ]
