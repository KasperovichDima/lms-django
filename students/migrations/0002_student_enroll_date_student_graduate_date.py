# Generated by Django 4.0 on 2021-12-14 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='enroll_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='student',
            name='graduate_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]