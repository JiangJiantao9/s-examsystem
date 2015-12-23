# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0023_auto_20151204_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='score',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='choicequestionans',
            name='state',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='fillquestionans',
            name='state',
            field=models.NullBooleanField(default=None),
        ),
    ]
