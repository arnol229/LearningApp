# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-07 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_last_edited_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='last_edited_by',
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]
