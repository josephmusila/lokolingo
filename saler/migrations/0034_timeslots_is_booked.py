# Generated by Django 5.0 on 2023-12-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("saler", "0033_timeslots"),
    ]

    operations = [
        migrations.AddField(
            model_name="timeslots",
            name="is_booked",
            field=models.BooleanField(default=False),
        ),
    ]