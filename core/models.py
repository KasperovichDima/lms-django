import random
from datetime import date
from datetime import datetime

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from groups.models import Group


class Person(models.Model):
    class Meta:
        abstract = True

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
        # validators=[AdultValidator(21)]
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True
    )

    def __full_name(self):
        return f'{self.first_name}, {self.last_name}'

    def __str__(self):
        return f'{self.__full_name()}, {self.birthday}'

    def save(self, *args, **kwargs):
        if isinstance(self.birthday, str):
            self.birthday = datetime.strptime(self.birthday, '%Y-%m-%d')
        self.age = relativedelta(date.today(), self.birthday).years
        super().save(*args, **kwargs)

    @classmethod
    def _generate(cls):
        fake = Faker()
        obj = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            birthday=fake.date_between_dates(date(1970, 1, 1), date(2000, 1, 1)),
            phone_number='380' + f'{random.choice([50, 95, 67, 97, 63, 73])}' +
            f'{random.choice(range(1000000, 9999999))}',
            )

        obj.save()
        return obj

    @classmethod
    def generate(cls, count):
        groups = Group.objects.all()
        if groups:
            for _ in range(count):
                group = random.choice(groups)
                cls._generate(group)
        else:
            print('There are no groups to attach. Create groups first, '
                  'using "python manage.py generate_groups [num, def=10]"!')
