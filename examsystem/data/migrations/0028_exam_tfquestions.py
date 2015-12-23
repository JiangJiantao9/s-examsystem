# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0027_point_tfquestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='tfquestions',
            field=models.ManyToManyField(to='data.TfQuestion', through='data.TfQuestionDetail', blank=True),
        ),
    ]
