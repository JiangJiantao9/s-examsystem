# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
