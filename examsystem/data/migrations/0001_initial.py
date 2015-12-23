# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=1, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D')])),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=1, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D')])),
                ('diffculty', models.CharField(max_length=2, choices=[(b'ez', b'easy'), (b'nm', b'normal'), (b'hd', b'hard')])),
                ('date', models.DateTimeField(verbose_name=b'date input')),
            ],
        ),
        migrations.CreateModel(
            name='FillQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('ans', models.CharField(max_length=200)),
                ('diffculty', models.CharField(max_length=2, choices=[(b'ez', b'easy'), (b'nm', b'normal'), (b'hd', b'hard')])),
                ('date', models.DateTimeField(verbose_name=b'date input')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='data.ChoiceQuestion'),
        ),
    ]
