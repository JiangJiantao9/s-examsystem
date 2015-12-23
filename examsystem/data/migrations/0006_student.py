# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20151027_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('num', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=1, choices=[(b'm', b'\xe7\x94\xb7'), (b'f', b'\xe5\xa5\xb3')])),
                ('birth', models.DateField(blank=True)),
                ('college', models.CharField(max_length=10, choices=[(b'\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba', b'\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba\xe5\xad\xa6\xe9\x99\xa2'), (b'\xe8\xbd\xaf\xe4\xbb\xb6', b'\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xad\xa6\xe9\x99\xa2')])),
                ('tel', models.CharField(max_length=15, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
            ],
        ),
    ]
