from django.urls import path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView)

from django.contrib.auth.decorators import login_required

from userprofile.views.userauth import UserRegisterView, UserChangeView

urlpatterns = [
    path('', UserRegisterView.as_view(), name='register')
]
