# Generated by Django 4.0 on 2021-12-23 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_rename_course_name_group_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]