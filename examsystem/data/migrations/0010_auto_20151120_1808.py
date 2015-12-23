# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20151120_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birth',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='college',
            field=models.CharField(max_length=10, null=True, choices=[(b'\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba', b'\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba\xe5\xad\xa6\xe9\x99\xa2'), (b'\xe8\xbd\xaf\xe4\xbb\xb6', b'\xe8\xbd\xaf\xe4\xbb\xb6\xe5\xad\xa6\xe9\x99\xa2')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='num',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sex',
            field=models.CharField(max_length=1, null=True, choices=[(b'm', b'\xe7\x94\xb7'), (b'f', b'\xe5\xa5\xb3')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='tel',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
