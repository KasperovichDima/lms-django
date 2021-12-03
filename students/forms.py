from django import forms
from django.core.validators import ValidationError

from .models import Student


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'phone_number',
        ]

        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'})}

    @staticmethod
    def normalize_name(arg):
        return arg.lower().capitalize()

    @staticmethod
    def normalize_phone(phone):
        """
        Normalization and validation of phone number from user
        :param phone: symbols from field "Phone number"
        :return: normalized phone number or raise ValidationError
        """
        normal_phone_length = 12

        # check for invalid characters
        if phone and not phone.isdigit():
            for symbol in phone:
                if not symbol.isdigit():
                    phone = phone.replace(symbol, '')

        # None check, length check and transformation to "380"
        if phone in ('', None):
            return None

        elif len(phone) < normal_phone_length and phone[0] == '8':
            phone = '3' + phone

        elif len(phone) < normal_phone_length and phone[0] == '0':
            phone = '38' + phone

        elif len(phone) > normal_phone_length or (len(phone) ==
                                                  normal_phone_length and phone[0] != '3'):
            raise ValidationError('Number is too long or incorrect. '
                                  'Please, check the number and try again!')

        elif len(phone) < normal_phone_length:
            raise ValidationError('Number is too short or incorrect. '
                                  'Please, check the number and try again!')

        return phone

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return self.normalize_name(first_name)

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return self.normalize_name(last_name)

    def clean_phone_number(self):
        """
        unique check of phone number
        :return: unique phone number for DB
        """
        phone_number = self.cleaned_data['phone_number']
        phone_number = self.normalize_phone(phone_number)
        if Student.objects.filter(phone_number=phone_number) and phone_number:
            raise ValidationError('This number is already in use. Please, try another one!')

        return phone_number
