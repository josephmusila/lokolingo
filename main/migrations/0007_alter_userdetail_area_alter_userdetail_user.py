# Generated by Django 5.0 on 2023-12-13 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_userdetail_locality"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdetail",
            name="area",
            field=models.CharField(
                choices=[("Beginner", "Beginner"), ("Intermediate", "Intermediate")],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="userdetail",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]