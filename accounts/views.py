from accounts import forms

import django.views.generic as CBV
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy


class AccountRegistrationView(CBV.CreateView):
    model = User
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('index')
    form_class = forms.AccountRegistrationForm


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        next_value = self.request.GET.get('next')
        if next_value:
            return next_value

        return reverse('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, f'User {self.request.user} has successfully logged in.')
        # messages.info(self.request, f'User {self.request.user} has successfully logged in.')
        # messages.warning(self.request, f'User {self.request.user} has successfully logged in.')
        # messages.error(self.request, f'User {self.request.user} has successfully logged in.')
        return result


class AccountLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


class AccountUpdateView(CBV.edit.ProcessFormView):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        profile = user.profile
        account_form = forms.AccountUpdateForm(instance=user)
        profile_form = forms.AccountProfileUpdateForm(instance=profile)

        return render(
            request,
            'accounts/profile.html',
            {
                'account_form': account_form,
                'profile_form': profile_form,
            }
        )

    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile = user.profile
        account_form = forms.AccountUpdateForm(instance=user, data=request.POST)
        profile_form = forms.AccountProfileUpdateForm(instance=profile, data=request.POST)

        if account_form.is_valid() and profile_form.is_valid():
            account_form.save()
            profile_form.save()

            return HttpResponseRedirect(reverse('accounts:profile'))

        else:
            return render(
                request,
                'accounts/profile.html',
                {
                    'account_form': account_form,
                    'profile_form': profile_form,
                }
            )
