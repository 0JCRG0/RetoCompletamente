# Generated by Django 4.2.2 on 2023-12-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DreamedJobAI", "0004_remove_stripecheckout_repeated_order_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stripecheckout",
            name="amount_total",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]