# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_initiative_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='initiative',
            name='email_validation',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='email',
            field=models.EmailField(null=True, blank=True, max_length=254, verbose_name='E-mail adress'),
        ),
    ]
