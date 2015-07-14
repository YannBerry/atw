# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0018_auto_20150715_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative',
            name='description',
            field=models.TextField(blank=True, max_length=350),
        ),
    ]
