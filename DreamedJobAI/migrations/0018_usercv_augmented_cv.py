# Generated by Django 4.2.2 on 2024-01-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DreamedJobAI", "0017_suitablejobstest"),
    ]

    operations = [
        migrations.AddField(
            model_name="usercv",
            name="augmented_cv",
            field=models.TextField(null=True),
        ),
    ]
