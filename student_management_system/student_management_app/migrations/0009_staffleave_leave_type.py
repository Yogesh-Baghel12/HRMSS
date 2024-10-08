# Generated by Django 5.1 on 2024-08-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student_management_app", "0008_staffleave"),
    ]

    operations = [
        migrations.AddField(
            model_name="staffleave",
            name="leave_type",
            field=models.CharField(
                choices=[("full_day", "Full Day"), ("half_day", "Half Day")],
                default="full_day",
                max_length=20,
            ),
        ),
    ]
