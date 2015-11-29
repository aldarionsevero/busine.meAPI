"""
Busine-me API
Universidade de Brasilia - FGA
Tecnicas de Programacao, 2/2015
@file models.py
Migrations based on user profiles.
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    """
    Class that creates migrations based on user profiles.
    """

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinemeUser',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        serialize=False, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(
                    verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(
                    null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', error_messages={'unique': 'A user with that username already exists.'}, validators=[
                 django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True, verbose_name='username', max_length=30)),
                ('first_name', models.CharField(max_length=30,
                                                verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30,
                                               verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254,
                                            verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False,
                                                 help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(
                    default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='date joined')),
                ('pontuation', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  blank=True, related_name='user_set', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='RankPosition',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        serialize=False, auto_created=True, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('min_points', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='businemeuser',
            name='rank',
            field=models.ForeignKey(
                null=True, to='authentication.RankPosition'),
        ),
        migrations.AddField(
            model_name='businemeuser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', help_text='Specific permissions for this user.',
                                         blank=True, related_name='user_set', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
