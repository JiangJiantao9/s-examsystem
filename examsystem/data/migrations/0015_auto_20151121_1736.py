# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_auto_20151121_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicequestionans',
            name='ans',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
