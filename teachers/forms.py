from core.normalizators import normalize_phone

from django import forms

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
        phone number check and normalization
        :return: correct phone number for DB
        """
        phone_number = self.cleaned_data['phone_number']
        phone_number = normalize_phone(phone_number)
        return phone_number
