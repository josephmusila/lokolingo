# Generated by Django 5.0 on 2023-12-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_rename_identification_userdetail_identification_document"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdetail",
            name="photo",
            field=models.FileField(upload_to="tutor_photos"),
        ),
    ]