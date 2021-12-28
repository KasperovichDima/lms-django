from core.normalizators import normalize_phone

from django import forms

from django_filters import FilterSet

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('age', 'enroll_date', 'graduate_date')
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


class StudentCreateForm(StudentForm):
    pass


class StudentUpdateForm(StudentForm):
    class Meta:
        model = Student
        exclude = ('age',)
        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'}),
                   'enroll_date': forms.DateInput(attrs={'type': 'date'}),
                   'graduate_date': forms.DateInput(attrs={'type': 'date'})
                   }


class StudentsFilter(FilterSet):
    class Meta:
        model = Student
        fields = {
            'age': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
            'group': ['exact']
        }
