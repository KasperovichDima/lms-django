# Generated by Django 3.2.9 on 2021-12-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('specialization', models.CharField(max_length=100)),
                ('work_experience', models.IntegerField()),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
        ),
    ]
