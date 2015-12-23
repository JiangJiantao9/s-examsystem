# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0020_auto_20151121_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='count',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
