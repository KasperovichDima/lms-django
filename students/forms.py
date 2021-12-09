from django import forms

from core.normalizators import normalize_phone
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

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return self.normalize_name(first_name)

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return self.normalize_name(last_name)

    def clean_phone_number(self):
        """
        phone number check and normalization
        :return: correct phone number for DB
        """
        phone_number = self.cleaned_data['phone_number']
        phone_number = normalize_phone(phone_number)
        return phone_number
