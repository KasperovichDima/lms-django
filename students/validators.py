import datetime

from django.core.validators import ValidationError

import students.models


def adult_validator(birthday):
    age = datetime.date.today().year - birthday.year
    ad_age = 18
    if age < ad_age:
        raise ValidationError('Must be 18 y.o. and older')


def phone_validator(phone_number):
    if students.models.Student.objects.filter(phone_number=phone_number).exists():
        raise ValidationError('This number is already in use. Please, try another one!')
