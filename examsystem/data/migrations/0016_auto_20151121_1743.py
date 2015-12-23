# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_auto_20151121_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicequestionans',
            name='ans',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
