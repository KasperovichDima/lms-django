from accounts.models import Profile

from django import forms as d_forms
from django.contrib.auth import forms


class AccountRegistrationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class AccountUpdateForm(forms.UserChangeForm):
    password = None

    class Meta(forms.UserCreationForm.Meta):
        fields = [
            'first_name',
            'last_name',
            'email',
        ]


class AccountProfileUpdateForm(d_forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthday', 'city']
        widgets = {'birthday': d_forms.DateInput(attrs={'type': 'date'})}
