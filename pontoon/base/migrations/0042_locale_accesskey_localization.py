# Generated by Django 3.2.15 on 2023-05-11 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0041_alter_userprofile_visibility_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="locale",
            name="accesskey_localization",
            field=models.BooleanField(
                default=True,
                help_text="\n        Allow localization of access keys if they are part of a string.\n        Some locales don't translate access keys, mostly because they use non-Latin scripts.\n    ",
            ),
        ),
    ]