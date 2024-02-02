# Generated by Django 4.2.2 on 2024-01-17 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DreamedJobAI", "0016_suitablejobs_hide"),
    ]

    operations = [
        migrations.CreateModel(
            name="SuitableJobsTest",
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
                ("job_id", models.IntegerField()),
                ("title", models.TextField()),
                ("link", models.TextField()),
                ("location", models.TextField()),
                ("pubdate", models.DateTimeField()),
                ("summary", models.TextField()),
                ("user_id", models.IntegerField()),
                ("suitability", models.TextField()),
                ("explanation", models.TextField()),
                (
                    "optimized_cv",
                    models.FileField(blank=True, null=True, upload_to="optimized_cv/"),
                ),
                ("vote", models.CharField(blank=True, max_length=4, null=True)),
                ("hide", models.BooleanField(default=False)),
                ("feedback", models.TextField(blank=True, null=True)),
                ("applied", models.BooleanField(default=False)),
                ("interview", models.BooleanField(default=False)),
                ("offer", models.BooleanField(default=False)),
            ],
        ),
    ]
