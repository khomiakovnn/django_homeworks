# Generated by Django 4.1.4 on 2022-12-09 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_student_teachers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]
