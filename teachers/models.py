from django.db import models

from .validators import phone_validator


class Teacher(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    specialization = models.CharField(max_length=100)
    work_experience = models.IntegerField()
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[phone_validator]
    )

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.age}, ' \
               f'{self.specialization}, {self.work_experience}, {self.phone_number}'
