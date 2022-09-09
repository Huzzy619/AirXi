from django.contrib.auth.views import (PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView)
from django.urls import path

from .views import ResetPassword, login_view, logout_view, register

urlpatterns = [

    path('register', register, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('password-reset', ResetPassword.as_view(
        template_name='accounts/password_reset.html'), name='password_reset'),

    path('password-reset-done', PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'),
        
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password-reset-complete', PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),




]
