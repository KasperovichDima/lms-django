import accounts.views as a_v

from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('registration/', a_v.AccountRegistrationView.as_view(), name='registration'),
    path('login/', a_v.AccountLoginView.as_view(), name='login'),
    path('logout/', a_v.AccountLogoutView.as_view(), name='logout'),
]
