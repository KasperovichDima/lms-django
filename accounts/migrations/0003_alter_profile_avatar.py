# Generated by Django 4.0 on 2022-01-18 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='avatars/'),
        ),
    ]
