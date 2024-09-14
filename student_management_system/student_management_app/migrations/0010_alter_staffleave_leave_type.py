# Generated by Django 5.1 on 2024-08-23 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student_management_app", "0009_staffleave_leave_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staffleave",
            name="leave_type",
            field=models.CharField(
                choices=[("full day", "Full Day"), ("half day", "Half Day")],
                default="full day",
                max_length=20,
            ),
        ),
    ]
