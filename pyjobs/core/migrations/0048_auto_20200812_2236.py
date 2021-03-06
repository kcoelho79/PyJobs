# Generated by Django 2.2.13 on 2020-08-12 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0047_auto_20200327_1316"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="consultancy",
            field=models.BooleanField(default=False, verbose_name="Consultoria?"),
        ),
        migrations.AlterField(
            model_name="job",
            name="contract_form",
            field=models.IntegerField(
                choices=[(1, "A combinar"), (2, "CLT"), (3, "PJ"), (4, "Estágio")],
                default=1,
                verbose_name="Forma de contratação",
            ),
        ),
    ]
