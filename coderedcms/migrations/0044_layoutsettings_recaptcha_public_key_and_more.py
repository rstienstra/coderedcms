# Generated by Django 4.2.19 on 2025-02-11 23:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coderedcms", "0043_remove_coderedpage_struct_org_actions_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="layoutsettings",
            name="recaptcha_public_key",
            field=models.CharField(
                blank=True,
                help_text="Create this key in the Google reCAPTCHA or Google Cloud dashboard.",
                max_length=255,
                verbose_name="reCAPTCHA Site Key (Public)",
            ),
        ),
        migrations.AddField(
            model_name="layoutsettings",
            name="recaptcha_secret_key",
            field=models.CharField(
                blank=True,
                help_text="Create this key in the Google reCAPTCHA or Google Cloud dashboard.",
                max_length=255,
                verbose_name="reCAPTCHA Secret Key (Private)",
            ),
        ),
        migrations.AddField(
            model_name="layoutsettings",
            name="recaptcha_threshold",
            field=models.DecimalField(
                decimal_places=1,
                default=0.5,
                help_text="reCAPTCHA v3 returns a score (0.0 is very likely a bot, 1.0 is very likely a good interaction). Reject submissions below this score (recommended 0.5).",
                max_digits=2,
                verbose_name="reCAPTCHA Threshold",
            ),
        ),
        migrations.AddField(
            model_name="layoutsettings",
            name="spam_service",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "None"),
                    ("honeypot", "Basic - honeypot technique"),
                    ("recaptcha3", "reCAPTCHA v3 - Invisible (requires API key)"),
                    (
                        "recaptcha2",
                        "reCAPTCHA v2 - I am not a robot (requires API key)",
                    ),
                ],
                default="honeypot",
                help_text="Choose a technique or 3rd party service to help block spam submissions.",
                max_length=10,
                verbose_name="Spam Protection",
            ),
        ),
    ]
