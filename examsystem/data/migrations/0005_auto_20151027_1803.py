# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceQuestionDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mark', models.IntegerField()),
                ('choicequestion', models.ForeignKey(to='data.ChoiceQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('diffculty', models.CharField(max_length=2, choices=[(b'ez', b'easy'), (b'nm', b'normal'), (b'hd', b'hard')])),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'date_input')),
                ('choicequestions', models.ManyToManyField(to='data.ChoiceQuestion', through='data.ChoiceQuestionDetail', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FillQuestionDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mark', models.IntegerField()),
                ('choicequestion', models.ForeignKey(to='data.FillQuestion')),
                ('exam', models.ForeignKey(to='data.Exam')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='fillquestions',
            field=models.ManyToManyField(to='data.FillQuestion', through='data.FillQuestionDetail', blank=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(to='data.Point'),
        ),
        migrations.AddField(
            model_name='choicequestiondetail',
            name='exam',
            field=models.ForeignKey(to='data.Exam'),
        ),
    ]
