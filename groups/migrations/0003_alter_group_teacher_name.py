# Generated by Django 4.0 on 2021-12-16 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_create_datetime_group_update_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='teacher_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
