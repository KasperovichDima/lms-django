import datetime

from django.core.validators import ValidationError
from django.utils.deconstruct import deconstructible


def adult_validator(birthday, age_limit=18):
    age = datetime.date.today().year - birthday.year
    if age < age_limit:
        raise ValidationError(f'Must be {age_limit} y.o. and older')

@deconstructible
class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    def __call__(self, *args, **kwargs):
        adult_validator(args[0], self.age_limit)

    def __eq__(self, other):
        return isinstance(other, AdultValidator) and self.age_limit == other.age_limit
