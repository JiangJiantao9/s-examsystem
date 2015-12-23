# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0028_exam_tfquestions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SAQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('diffculty', models.CharField(max_length=2, choices=[(b'ez', b'easy'), (b'nm', b'normal'), (b'hd', b'hard')])),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'date input')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SAQuestionAns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ans', models.CharField(max_length=200, null=True)),
                ('state', models.NullBooleanField(default=None)),
                ('SAquestion', models.ForeignKey(to='data.SAQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='SAQuestionDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mark', models.IntegerField()),
                ('SAquestion', models.ForeignKey(to='data.SAQuestion')),
                ('exam', models.ForeignKey(to='data.Exam')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='Tfquestion',
            field=models.ManyToManyField(to='data.TfQuestion', through='data.TfQuestionAns'),
        ),
        migrations.AddField(
            model_name='saquestionans',
            name='answer',
            field=models.ForeignKey(to='data.Answer'),
        ),
        migrations.AddField(
            model_name='answer',
            name='SAquestion',
            field=models.ManyToManyField(to='data.SAQuestion', through='data.SAQuestionAns'),
        ),
        migrations.AddField(
            model_name='exam',
            name='SAquestions',
            field=models.ManyToManyField(to='data.SAQuestion', through='data.SAQuestionDetail', blank=True),
        ),
    ]
