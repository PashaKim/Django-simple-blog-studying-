# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(verbose_name='Добавить комментарий'),
        ),
    ]
