# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-18 05:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0006_auto_20181217_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploads.Image'),
        ),
    ]