# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0024_auto_20151204_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='fill_score',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='select_score',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
