# Generated by Django 4.0 on 2021-12-23 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_rename_course_name_group_group_name'),
        ('courses', '0002_course_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='group',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='groups.group'),
        ),
    ]
