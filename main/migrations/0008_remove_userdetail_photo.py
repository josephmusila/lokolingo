# Generated by Django 5.0 on 2023-12-14 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_alter_userdetail_area_alter_userdetail_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userdetail",
            name="photo",
        ),
    ]