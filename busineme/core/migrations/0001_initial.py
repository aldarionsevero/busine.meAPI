"""
Busine-me API
Universidade de Brasilia - FGA
Tecnicas de Programacao, 2/2015
@file models.py
Migrations based on user buslines.
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    """
    Class that creates migrations based on buslines.
    """

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Busline',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        serialize=False, auto_created=True, verbose_name='ID')),
                ('line_number', models.CharField(unique=True, max_length=5)),
                ('description', models.CharField(max_length=255)),
                ('via', models.CharField(max_length=255)),
                ('route_size', models.FloatField()),
                ('fee', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        serialize=False, auto_created=True, verbose_name='ID')),
                ('busline', models.ForeignKey(to='core.Busline')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        serialize=False, auto_created=True, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('traffic', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('busline', models.ForeignKey(to='core.Busline')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        serialize=False, auto_created=True, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('address', models.CharField(null=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='busline',
            name='company',
            field=models.ForeignKey(null=True, to='core.Company'),
        ),
        migrations.AddField(
            model_name='busline',
            name='terminals',
            field=models.ManyToManyField(to='core.Terminal'),
        ),
    ]
