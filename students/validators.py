import datetime

# from .models import Student

from django.core.validators import ValidationError


def adult_validator(birthday):
    age = datetime.date.today().year - birthday.year
    ad_age = 18
    if age < ad_age:
        raise ValidationError('Must be 18 y.o. and older')
