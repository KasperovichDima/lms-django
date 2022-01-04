from accounts.forms import AccountRegistrationForm

import django.views.generic as CBV
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse
from django.urls import reverse_lazy


class AccountRegistrationView(CBV.CreateView):
    model = User
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('index')
    form_class = AccountRegistrationForm


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        next_value = self.request.GET.get('next')
        if next_value:
            return next_value

        return reverse('index')


class AccountLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
