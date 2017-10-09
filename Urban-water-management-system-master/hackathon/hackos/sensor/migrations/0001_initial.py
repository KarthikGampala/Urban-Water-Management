# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soil_value', models.CharField(max_length=250)),
                ('water_level', models.CharField(max_length=250)),
                ('water_flow', models.CharField(max_length=250)),
                ('turbidity', models.CharField(max_length=250)),
                ('ph', models.CharField(max_length=250)),
            ],
        ),
    ]
