# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-17 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("core", "0023_auto_20190217_1831")]

    operations = [
        migrations.AddField(
            model_name="jobapplication",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        )
    ]