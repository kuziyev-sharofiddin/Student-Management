# Generated by Django 3.1.14 on 2022-07-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0015_student_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_feedback',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]