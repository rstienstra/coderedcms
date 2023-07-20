# Generated by Django 4.1.7 on 2023-03-30 19:14

import coderedcms.fields
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("coderedcms", "0035_remove_googleapisettings_site_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FilmStrip",
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
                ("name", models.CharField(max_length=255, verbose_name="Name")),
            ],
            options={
                "verbose_name": "Film Strip",
            },
        ),
        migrations.CreateModel(
            name="FilmPanel",
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
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "background_color",
                    models.CharField(
                        blank=True,
                        help_text="Hexadecimal, rgba, or CSS color notation (e.g. #ff0011)",
                        max_length=255,
                        verbose_name="Background color",
                    ),
                ),
                (
                    "foreground_color",
                    models.CharField(
                        blank=True,
                        help_text="Hexadecimal, rgba, or CSS color notation (e.g. #ff0011)",
                        max_length=255,
                        verbose_name="Text color",
                    ),
                ),
                (
                    "custom_css_class",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        verbose_name="Custom CSS class",
                    ),
                ),
                (
                    "custom_id",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Custom ID"
                    ),
                ),
                (
                    "content",
                    coderedcms.fields.CoderedStreamField(
                        blank=True, use_json_field=True
                    ),
                ),
                (
                    "background_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Background image",
                    ),
                ),
                (
                    "film_strip",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="film_panels",
                        to="coderedcms.filmstrip",
                        verbose_name="Film Panel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Film Panel",
            },
        ),
    ]