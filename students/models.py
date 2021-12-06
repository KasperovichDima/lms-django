import datetime

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from .validators import adult_validator
from .validators import phone_validator


class Student(models.Model):

    first_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    last_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    age = models.IntegerField()
    birthday = models.DateField(
        default=datetime.date.today,
        validators=[adult_validator])
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[phone_validator]
    )

    def save(self, *args, **kwargs):
        self.age = relativedelta(datetime.date.today(), self.birthday).years
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.age}, {self.phone_number}'

    @staticmethod
    def generate_students(request):
        """
        generates random students and saves them to db
        :param request: url parameter 'count'
        default = 10
        :return:
        """
        num = 10  # default number of students to generate

        if 'count' in request.GET:
            if request.GET['count'].isdigit():
                num = int(request.GET['count'])

        fake = Faker()
        for _ in range(num):
            std = Student(first_name=fake.first_name(),
                          last_name=fake.last_name(),
                          age=fake.pyint(15, 75))
            std.save()

        return f'<h1>{num} students generated!</h1>'
