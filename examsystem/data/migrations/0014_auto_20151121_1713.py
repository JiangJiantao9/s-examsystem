# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_auto_20151121_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'date_input')),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceQuestionAns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ans', models.CharField(max_length=1)),
                ('answer', models.ForeignKey(to='data.Answer')),
                ('choicequestion', models.ForeignKey(to='data.ChoiceQuestion')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='choicequestion',
            field=models.ManyToManyField(to='data.ChoiceQuestion', through='data.ChoiceQuestionAns'),
        ),
        migrations.AddField(
            model_name='answer',
            name='exam',
            field=models.ForeignKey(to='data.Exam'),
        ),
    ]
