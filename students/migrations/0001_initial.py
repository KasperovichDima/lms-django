# Generated by Django 4.0 on 2021-12-21 16:00

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('age', models.IntegerField()),
                ('birthday', models.DateField(default=datetime.date.today)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('enroll_date', models.DateField(default=datetime.date.today)),
                ('graduate_date', models.DateField(default=datetime.date.today)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='groups.group')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
