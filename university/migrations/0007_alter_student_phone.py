# Generated by Django 4.2.2 on 2023-06-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0006_student_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.BigIntegerField(max_length=11),
        ),
    ]
