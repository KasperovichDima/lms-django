# Generated by Django 4.0 on 2021-12-22 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='number_of_students',
        ),
    ]
