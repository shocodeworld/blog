# Generated by Django 4.1.2 on 2022-11-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_post_main_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="main_image",
            field=models.ImageField(blank=True, null=True, upload_to="posts_images/"),
        ),
    ]
