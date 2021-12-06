from django.core.validators import ValidationError

import teachers.models


def phone_validator(phone_number):
    if teachers.models.Teacher.objects.filter(phone_number=phone_number).exists():
        raise ValidationError('This number is already in use. Please, try another one!')
