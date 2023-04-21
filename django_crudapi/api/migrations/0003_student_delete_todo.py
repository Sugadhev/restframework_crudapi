# Generated by Django 4.2 on 2023-04-21 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_todo_dateofbirth_alter_todo_mobilenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=50)),
                ('Rollno', models.IntegerField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('MobileNumber', models.BigIntegerField(max_length=50)),
                ('DateOfBirth', models.DateField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
