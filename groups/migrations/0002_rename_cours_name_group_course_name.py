# Generated by Django 3.2.9 on 2021-11-30 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='cours_name',
            new_name='course_name',
        ),
    ]
