# Generated by Django 3.2.12 on 2022-03-02 08:50
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BillBasic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bill_id",
                    models.CharField(max_length=20, verbose_name="bill_id"),
                ),
                (
                    "bill_type",
                    models.CharField(
                        choices=[
                            ("hr", "H.R. 1234"),
                            ("hres", "H.Res. 1234"),
                            ("hconres", "H.Con.Res. 1234"),
                            ("hjres", "H.J.Res. 1234"),
                            ("s", "S. 1234"),
                            ("sres", "S.Res. 1234"),
                            ("sconres", "S.Con.Res. 1234"),
                            ("sjres", "S.J.Res. 1234"),
                        ],
                        max_length=10,
                        verbose_name="bill_type",
                    ),
                ),
                ("number", models.IntegerField(verbose_name="number")),
                (
                    "bill_number",
                    models.CharField(max_length=20, verbose_name="bill_number"),
                ),
                ("congress", models.IntegerField(verbose_name="congress")),
                (
                    "introduced_at",
                    models.DateField(verbose_name="introduction date"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(verbose_name="updated time"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BillTitles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "official_title",
                    models.CharField(
                        blank=True,
                        max_length=2000,
                        null=True,
                        verbose_name="official_title",
                    ),
                ),
                (
                    "popular_title",
                    models.CharField(
                        blank=True,
                        max_length=2000,
                        null=True,
                        verbose_name="popular_title",
                    ),
                ),
                (
                    "short_title",
                    models.CharField(
                        blank=True,
                        max_length=2000,
                        null=True,
                        verbose_name="short_title",
                    ),
                ),
                (
                    "bill_basic",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="billtitles",
                        to="btiapp.billbasic",
                        verbose_name="bill_basic",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BillStageTitle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=2000, verbose_name="title"),
                ),
                (
                    "titleNoYear",
                    models.CharField(max_length=2000, verbose_name="titleNoYear"),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("O", "official"),
                            ("P", "popular"),
                            ("S", "short"),
                        ],
                        max_length=10,
                        verbose_name="type",
                    ),
                ),
                (
                    "As",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="as"
                    ),
                ),
                (
                    "is_for_portion",
                    models.BooleanField(verbose_name="is_for_portion"),
                ),
                (
                    "bill_basic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="billstagetitle",
                        to="btiapp.billbasic",
                        verbose_name="bill_basic",
                    ),
                ),
            ],
        ),
    ]
