from django import forms

from django_filters import FilterSet

from .models import Group


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'})}


class GroupCreateForm(GroupBaseForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'start_date',
            'teachers',
        ]
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'})}


class GroupUpdateForm(GroupBaseForm):
    class Meta:
        model = Group
        fields = '__all__'
        exclude = ['headman', ]
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hdmn'] = forms.ChoiceField(
            choices=[(student.id, str(student)) for student in self.instance.students.all()],
            label='Choose headman-student in this group:',
            required=False
        )


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
