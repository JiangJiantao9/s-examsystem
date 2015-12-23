# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0021_exam_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='count',
            field=models.IntegerField(default=100),
        ),
    ]
