# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medhistory', '0002_history_blood_sugar_level'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ['-time']},
        ),
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]