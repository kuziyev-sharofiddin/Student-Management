# Generated by Django 3.1.14 on 2022-07-06 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0010_staff_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_leave',
            name='status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='staff_notification',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
