# Generated by Django 3.2.9 on 2021-12-02 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birthday',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
