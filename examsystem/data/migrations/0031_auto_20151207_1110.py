# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0030_auto_20151207_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='sa_score',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='tf_score',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
