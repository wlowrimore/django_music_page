# Generated by Django 4.2.3 on 2023-07-12 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_remove_profile_profile_pic_profile_profile_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="first_name",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="profile",
            name="last_name",
            field=models.CharField(default="", max_length=50),
        ),
    ]