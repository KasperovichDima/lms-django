from django import forms

from django_filters import FilterSet

from .models import Group


class GroupsCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'start_date',
            'teachers',
        ]
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'})}


class GroupsUpdateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'})}


class GroupsFilter(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', ],
            'course': ['exact', ],
            'start_date': ['month__lt', 'month__gt'],
            'headman': ['exact', ],
            'teachers': ['exact', ]
        }
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'})}
