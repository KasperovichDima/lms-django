from django import forms

from .models import Group


class GroupsCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'course_name',
            'start_date',
            'number_of_students',
            'teacher_name',
        ]

        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'})}
