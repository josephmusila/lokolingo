# Generated by Django 5.0 on 2023-12-22 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("saler", "0052_alter_bookingpayments_booking"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="tutor",
        ),
    ]