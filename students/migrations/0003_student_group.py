# Generated by Django 4.0 on 2021-12-15 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_create_datetime_group_update_datetime'),
        ('students', '0002_student_enroll_date_student_graduate_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='groups.group'),
        ),
    ]
