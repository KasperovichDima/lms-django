# Generated by Django 3.2.9 on 2021-12-03 10:12

import datetime
import django.core.validators
from django.db import migrations, models
import core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(default=datetime.date.today, validators=[core.validators.adult_validator]),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
