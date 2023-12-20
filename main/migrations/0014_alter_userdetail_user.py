# Generated by Django 5.0 on 2023-12-16 09:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0013_alter_userdetail_photo"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdetail",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                related_name="userdetails",
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]