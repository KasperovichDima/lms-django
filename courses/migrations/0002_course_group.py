# Generated by Django 4.0 on 2021-12-23 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_rename_course_name_group_group_name'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='group',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course', to='groups.group'),
        ),
    ]
