# Generated by Django 4.2.3 on 2023-07-12 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_profile_first_name_profile_last_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="description",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="last_name",
        ),
        migrations.AlterField(
            model_name="profile",
            name="profile_img",
            field=models.ImageField(default="no_image.png", upload_to=""),
        ),
    ]
