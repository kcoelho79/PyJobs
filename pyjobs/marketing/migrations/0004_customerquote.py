# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-14 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marketing", "0003_auto_20191104_1326"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerQuote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "customer_name",
                    models.CharField(max_length=500, verbose_name="Nome do cliente"),
                ),
                (
                    "company_name",
                    models.CharField(max_length=500, verbose_name="Nome da empresa"),
                ),
                (
                    "avatar_name",
                    models.CharField(
                        max_length=500, verbose_name="Nome da imagem estatica do avatar"
                    ),
                ),
                (
                    "customer_quote",
                    models.TextField(verbose_name="Texto do depoimento"),
                ),
            ],
        ),
    ]
