import random
from datetime import date
from datetime import timedelta

from core.validators import AdultValidator

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from groups.models import Group


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
        default=date.today,
        validators=[AdultValidator(21)]
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )
    enroll_date = models.DateField(default=date.today)
    graduate_date = models.DateField(default=date.today)

    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True
    )

    def save(self, *args, **kwargs):
        self.age = relativedelta(date.today(), self.birthday).years
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
        group = Group.objects.all()

        for _ in range(num):
            birthday = fake.date_between_dates(date(1970, 1, 1), date(2000, 1, 1))
            enroll_date = fake.date_between_dates(date(2021, 10, 1), date.today())

            std = Student(first_name=fake.first_name(),
                          last_name=fake.last_name(),
                          birthday=birthday,
                          age=date.today() - birthday,
                          group=random.choice(group),
                          enroll_date=enroll_date,
                          graduate_date=enroll_date+timedelta(days=120),
                          phone_number='380' + f'{random.choice([50,95,67,97,63,73])}' +
                                       f'{random.choice(range(1000000,9999999))}'
                          )
            std.save()

        return f'{num} students generated!'
