import datetime

from django.core.validators import ValidationError

import students.models


def adult_validator(birthday, age_limit=18):
    age = datetime.date.today().year - birthday.year
    if age < age_limit:
        raise ValidationError(f'Must be {age_limit} y.o. and older')


def phone_validator(phone_number):
    if students.models.Student.objects.filter(phone_number=phone_number).exists():
        raise ValidationError('This number is already in use. Please, try another one!')

class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    def __call__(self, *args, **kwargs):
        adult_validator(args[0], self.age_limit)