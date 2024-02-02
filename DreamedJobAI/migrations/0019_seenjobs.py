# Generated by Django 4.2.2 on 2024-01-24 21:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DreamedJobAI", "0018_usercv_augmented_cv"),
    ]

    operations = [
        migrations.CreateModel(
            name="SeenJobs",
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
                ("user_id", models.IntegerField()),
                ("job_id", models.IntegerField()),
                ("suitability", models.TextField()),
                ("explanation", models.TextField()),
            ],
        ),
    ]