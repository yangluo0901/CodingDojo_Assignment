# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-13 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
