# Generated by Django 5.0 on 2023-12-17 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0039_merge_20231217_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslots',
            name='meet_url',
        ),
        migrations.RemoveField(
            model_name='timeslots',
            name='student',
        ),
    ]