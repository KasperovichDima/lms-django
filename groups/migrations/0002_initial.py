# Generated by Django 4.0 on 2021-12-21 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
        ('groups', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='headman',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='headman_in_group', to='students.student'),
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ManyToManyField(related_name='groups', to='teachers.Teacher'),
        ),
    ]
