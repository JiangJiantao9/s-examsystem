# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20151026_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('choicequestions', models.ManyToManyField(to='data.ChoiceQuestion', blank=True)),
                ('fillquestions', models.ManyToManyField(to='data.FillQuestion', blank=True)),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='data.Point', null=True)),
            ],
        ),
    ]
