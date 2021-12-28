from core.normalizators import normalize_phone

from django import forms

from django_filters import FilterSet

from .models import Teacher


class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ('age',)
        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'})}

    def clean_phone_number(self):
        """
        phone number check and normalization
        :return: correct phone number for DB
        """
        phone_number = self.cleaned_data['phone_number']
        phone_number = normalize_phone(phone_number)
        return phone_number


class TeachersCreateForm(TeachersForm):
    pass


class TeachersUpdateForm(TeachersForm):
    pass


class TeachersFilter(FilterSet):
    class Meta:
        model = Teacher
        exclude = ['age', 'phone_number']
