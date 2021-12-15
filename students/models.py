import datetime

from core.validators import AdultValidator

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker


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
        validators=[AdultValidator(21)]
    )
    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)

    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True
    )

    def save(self, *args, **kwargs):
        self.age = relativedelta(datetime.date.today(), self.birthday).years
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, ' \
               f'{self.age}, {self.birthday}, {self.phone_number}'

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

        return f'{num} students generated!'
