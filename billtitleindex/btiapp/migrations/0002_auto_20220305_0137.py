# Generated by Django 3.2.12 on 2022-03-05 01:37
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("btiapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="billstagetitle",
            name="is_for_portion",
            field=models.BooleanField(
                blank=True, null=True, verbose_name="is_for_portion"
            ),
        ),
        migrations.AlterField(
            model_name="billstagetitle",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[("O", "official"), ("P", "popular"), ("S", "short")],
                max_length=10,
                null=True,
                verbose_name="type",
            ),
        ),
    ]
