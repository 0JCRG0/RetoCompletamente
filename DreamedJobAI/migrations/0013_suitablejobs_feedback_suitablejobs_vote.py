# Generated by Django 4.2.2 on 2024-01-10 05:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DreamedJobAI", "0012_suitablejobs_optimized_cv"),
    ]

    operations = [
        migrations.AddField(
            model_name="suitablejobs",
            name="feedback",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="suitablejobs",
            name="vote",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]