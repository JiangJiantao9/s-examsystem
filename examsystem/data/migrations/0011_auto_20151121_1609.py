# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_auto_20151120_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='choicequestion',
            name='user',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='fillquestion',
            name='user',
            field=models.IntegerField(null=True),
        ),
    ]
