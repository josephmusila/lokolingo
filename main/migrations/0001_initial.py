# Generated by Django 5.0 on 2024-01-04 15:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("date", models.DateField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=100)),
                ("message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Slider",
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
                ("name", models.CharField(default="", max_length=50, null=True)),
                ("image", models.ImageField(upload_to="slider_img")),
                ("url", models.CharField(default="#", max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="TutorUserDetails",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="tutordetails",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "contact_number",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "profile_picture",
                    models.FileField(
                        upload_to="tutor_images",
                        verbose_name="Upload A Professional Headshot",
                    ),
                ),
                (
                    "highiest_qualification",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("specialization", models.TextField()),
                ("years_of_experience", models.CharField(max_length=10)),
                ("teaching_style", models.TextField()),
                ("teaching_philosophy", models.TextField(blank=True, null=True)),
                (
                    "availability",
                    models.CharField(
                        choices=[
                            ("monday", "Monday"),
                            ("tuesday", "Tuesday"),
                            ("wednesday", "Wednesday"),
                            ("thursday", "Thursday"),
                            ("friday", "Friday"),
                            ("saturday", "Saturday"),
                            ("sunday", "Sunday"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "preferred_teaching_method",
                    models.CharField(
                        choices=[
                            ("one on one", "One on One"),
                            ("group sessions", "Group Sessions"),
                        ],
                        max_length=50,
                    ),
                ),
                ("hourly_rate", models.CharField(max_length=50)),
                ("preferred_payment_method", models.TextField()),
                ("education_materials_link", models.TextField()),
                ("languages_spoken", models.CharField(max_length=100)),
                ("special_certificate_skills", models.TextField()),
                ("cancellation_policy", models.TextField(blank=True, null=True)),
                ("terms_acceptance", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="UserDetail",
            fields=[
                (
                    "user_type",
                    models.CharField(
                        choices=[("student", "Student"), ("tutor", "Tutor")],
                        max_length=10,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="userdetails",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "rate_per_hour",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("profile_description", models.TextField()),
                (
                    "tutoring_experience",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                ("country", models.CharField(default="Kenya", max_length=100)),
                (
                    "identification_document",
                    models.FileField(upload_to="tutor_documents"),
                ),
                ("photo", models.FileField(upload_to="tutor_photos")),
                ("mobile", models.CharField(max_length=10, null=True)),
                (
                    "alternate_mobile",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                ("address", models.CharField(blank=True, max_length=100, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "sex",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Other", "Other"),
                        ],
                        max_length=6,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
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
                ("product_id", models.CharField(max_length=100)),
                (
                    "product_size",
                    models.CharField(default="", max_length=20, null=True),
                ),
                ("number", models.PositiveIntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TutorRating",
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
                ("rating", models.IntegerField()),
                ("review", models.CharField(max_length=200)),
                ("date_added", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="student",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tutor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="tutor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CertificateFile",
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
                ("file", models.FileField(upload_to="special_certs")),
                (
                    "tutor_user_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="special_certificate_files",
                        to="main.tutoruserdetails",
                    ),
                ),
            ],
        ),
    ]
