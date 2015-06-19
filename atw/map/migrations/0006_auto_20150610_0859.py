# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20150610_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative',
            name='email_validation',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
