# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0029_auto_20151207_1020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='SAquestion',
            new_name='saquestion',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='SAquestions',
            new_name='saquestions',
        ),
        migrations.RenameField(
            model_name='saquestionans',
            old_name='SAquestion',
            new_name='saquestion',
        ),
        migrations.RenameField(
            model_name='saquestiondetail',
            old_name='SAquestion',
            new_name='saquestion',
        ),
        migrations.AddField(
            model_name='point',
            name='saquestions',
            field=models.ManyToManyField(to='data.SAQuestion', blank=True),
        ),
    ]
