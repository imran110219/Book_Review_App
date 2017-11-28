# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_name', models.CharField(max_length=100)),
                ('publication_description', models.TextField(max_length=500)),
                ('publication_image', models.ImageField(height_field='height_field', upload_to='', width_field='width_field')),
                ('height_field', models.IntegerField(default=255)),
                ('width_field', models.IntegerField(default=255)),
            ],
        ),
    ]
