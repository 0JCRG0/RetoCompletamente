# Generated by Django 4.2.2 on 2023-12-29 00:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DreamedJobAI", "0010_blogpost"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="author",
            field=models.TextField(default="Maddy Vann", max_length=50),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="author_pp",
            field=models.ImageField(
                blank=True, default="blog/blog-author-pp-default.jpg", upload_to="blog/"
            ),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="category",
            field=models.TextField(default="Reverse Recruiting", max_length=50),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="thumbnail",
            field=models.ImageField(
                blank=True, default="blog/blog-thumbnail-default.jpg", upload_to="blog/"
            ),
        ),
    ]
