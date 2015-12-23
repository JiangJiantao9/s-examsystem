# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0026_tfquestion_tfquestionans_tfquestiondetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='tfquestions',
            field=models.ManyToManyField(to='data.TfQuestion', blank=True),
        ),
    ]
