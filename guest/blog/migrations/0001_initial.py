# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-27 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=150)),
                ('blog_content', models.TextField()),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('flag', models.CharField(max_length=150)),
            ],
        ),
    ]
