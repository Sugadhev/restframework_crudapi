# Generated by Django 4.2 on 2023-04-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_student_rollno_student_rollnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='StudentName',
            field=models.CharField(max_length=15),
        ),
    ]
