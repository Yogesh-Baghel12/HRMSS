# Generated by Django 4.2.2 on 2024-09-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0014_remove_employee_father_occupation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeleave',
            name='from_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employeeleave',
            name='to_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='staffleave',
            name='from_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='staffleave',
            name='to_date',
            field=models.DateField(),
        ),
    ]
