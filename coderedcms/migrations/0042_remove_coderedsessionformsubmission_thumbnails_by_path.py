# Generated by Django 4.2.16 on 2025-02-06 19:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("coderedcms", "0041_remove_layoutsettings_frontend_theme"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="coderedsessionformsubmission",
            name="thumbnails_by_path",
        ),
    ]
