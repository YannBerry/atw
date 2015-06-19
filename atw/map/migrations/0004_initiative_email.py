# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20150608_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='initiative',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail adress (displayed in your factsheet)', null=True, blank=True),
        ),
    ]
