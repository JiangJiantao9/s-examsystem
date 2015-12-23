# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20151026_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillquestion',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'date input'),
        ),
    ]
