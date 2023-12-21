# Generated by Django 5.0 on 2023-12-20 11:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_tutorrating_student_alter_tutorrating_tutor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorrating',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tutorrating',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tutor', to=settings.AUTH_USER_MODEL),
        ),
    ]