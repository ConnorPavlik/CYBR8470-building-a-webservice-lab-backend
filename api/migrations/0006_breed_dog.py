# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-27 02:50
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170905_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('friendliness', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('trainability', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('sheddingamount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('exerciseneeds', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('favoritefood', models.CharField(max_length=100)),
                ('favoritetoy', models.CharField(max_length=100)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Breed')),
            ],
        ),
    ]
