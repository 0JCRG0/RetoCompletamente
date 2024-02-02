# Generated by Django 4.2.2 on 2023-12-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DreamedJobAI", "0009_remove_usertokens_timestamp"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
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
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
                ("slug", models.SlugField(blank=True, max_length=255, unique=True)),
            ],
        ),
    ]