from django import forms
from django.core.validators import ValidationError

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

    @staticmethod
    def normalize_phone(phone):
        """
        Normalization of phone number from user
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

    def clean_phone_number(self):
        """
        phone number check and normalization
        :return: correct phone number for DB
        """
        phone_number = self.cleaned_data['phone_number']
        phone_number = self.normalize_phone(phone_number)
        return phone_number
