# Generated by Django 4.2.3 on 2023-07-13 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_remove_profile_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="bio",
            field=models.TextField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="profile",
            name="location",
            field=models.CharField(blank=True, max_length=101, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="first_name",
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name="profile",
            name="last_name",
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]