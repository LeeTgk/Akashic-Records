from django.urls import path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView)

from userprofile.views.userauth import UserRegisterView, UserChangeView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('change/', UserChangeView.as_view(), name='change'),
    path('login/', LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password/', PasswordChangeView.as_view(template_name='userprofile/password.html'), name='password_change'),
    path('password/done/', PasswordChangeDoneView.as_view(template_name='userprofile/password_done.html'), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
