# Generated by Django 5.0 on 2023-12-23 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("saler", "0054_booking_cost"),
    ]

    operations = [
        migrations.CreateModel(
            name="TutorSession",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "session_status",
                    models.CharField(
                        choices=[
                            ("not_started", "Not Started"),
                            ("ongoing", "Ongoing"),
                            ("completed", "Completed"),
                            ("pending_approval", "Pending Approval"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="not_started",
                        max_length=20,
                    ),
                ),
                ("meet_url", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "payments",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="saler.bookingpayments",
                    ),
                ),
            ],
        ),
    ]