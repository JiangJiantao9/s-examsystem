# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0031_auto_20151207_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='saquestionans',
            name='mark',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='saquestionans',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
