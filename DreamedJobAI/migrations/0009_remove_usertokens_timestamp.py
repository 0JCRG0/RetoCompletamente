# Generated by Django 4.2.2 on 2023-12-23 01:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("DreamedJobAI", "0008_alter_usertokens_timestamp"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usertokens",
            name="timestamp",
        ),
    ]
