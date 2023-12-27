# Generated by Django 5.0 on 2023-12-25 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_tutorrating_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='rate_per_hour',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='tutoring_experience',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]