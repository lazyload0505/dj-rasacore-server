# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasacore', '0015_auto_20171116_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='name',
            field=models.SlugField(max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='entities',
            name='name',
            field=models.SlugField(max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='intents',
            name='name',
            field=models.SlugField(max_length=70, unique=True),
        ),
    ]
