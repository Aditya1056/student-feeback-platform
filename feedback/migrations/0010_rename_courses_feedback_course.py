# Generated by Django 4.0.3 on 2022-07-21 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0009_remove_feedback_course_feedback_courses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='courses',
            new_name='course',
        ),
    ]
