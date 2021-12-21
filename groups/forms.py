from django import forms

from django_filters import FilterSet

from .models import Group


class GroupsForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'course_name',
            'start_date',
            'number_of_students',
            # 'teacher_name',
        ]

        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'})}


class GroupsFilter(FilterSet):
    class Meta:
        model = Group
        fields = {
            'course_name': ['exact', 'icontains'],
            'start_date': ['year__gt'],
            'number_of_students': ['lt', 'gt'],
            # 'teacher_name': ['exact', 'icontains'],
        }
