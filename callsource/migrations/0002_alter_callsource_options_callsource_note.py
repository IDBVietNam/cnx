# Generated by Django 4.2.17 on 2025-02-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("callsource", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="callsource",
            options={
                "verbose_name": "CallSource",
                "verbose_name_plural": "CallSources",
            },
        ),
        migrations.AddField(
            model_name="callsource",
            name="note",
            field=models.TextField(blank=True, null=True),
        ),
    ]
