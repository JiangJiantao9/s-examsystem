# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0025_auto_20151204_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='TfQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('ans', models.BooleanField()),
                ('diffculty', models.CharField(max_length=2, choices=[(b'ez', b'easy'), (b'nm', b'normal'), (b'hd', b'hard')])),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'date input')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TfQuestionAns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ans', models.NullBooleanField()),
                ('state', models.NullBooleanField(default=None)),
                ('Tfquestion', models.ForeignKey(to='data.TfQuestion')),
                ('answer', models.ForeignKey(to='data.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='TfQuestionDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mark', models.IntegerField()),
                ('exam', models.ForeignKey(to='data.Exam')),
                ('tfquestion', models.ForeignKey(to='data.TfQuestion')),
            ],
        ),
    ]
