from django import forms
from django.core.validators import ValidationError

from students.forms import StudentCreateForm

from .models import Teacher


class TeachersCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'age',
            'specialization',
            'work_experience',
            'phone_number',
        ]

    def clean_phone_number(self):
        """
        unique check of phone number
        :return: unique phone number for DB
        """
        phone_number = self.cleaned_data['phone_number']
        phone_number = StudentCreateForm.normalize_phone(phone_number)
        if Teacher.objects.filter(phone_number=phone_number) and phone_number:
            raise ValidationError('This number is already in use. Please, try another one!')

        return phone_number
