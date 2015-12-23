# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_auto_20151204_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='FillQuestionAns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ans', models.CharField(max_length=100, null=True)),
                ('answer', models.ForeignKey(to='data.Answer')),
                ('fillquestion', models.ForeignKey(to='data.FillQuestion')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='fillquestion',
            field=models.ManyToManyField(to='data.FillQuestion', through='data.FillQuestionAns'),
        ),
    ]
