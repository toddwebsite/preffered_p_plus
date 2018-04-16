from __future__ import unicode_literals

from django.urls import path, re_path

from account.views import SignupView, LoginView, LogoutView, DeleteView
from account.views import ConfirmEmailView
from account.views import ChangePasswordView, PasswordResetView, PasswordResetTokenView
from account.views import SettingsView, AgentList, AgentDetail


urlpatterns = [
    re_path(r"^signup/$", SignupView.as_view(), name="account_signup"),
    re_path(r"^login/$", LoginView.as_view(), name="account_login"),
    re_path(r"^logout/$", LogoutView.as_view(), name="account_logout"),
    re_path(r"^confirm_email/(?P<key>\w+)/$", ConfirmEmailView.as_view(), name="account_confirm_email"),
    re_path(r"^password/$", ChangePasswordView.as_view(), name="account_password"),
    re_path(r"^password/reset/$", PasswordResetView.as_view(), name="account_password_reset"),
    re_path(r"^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$", PasswordResetTokenView.as_view(), name="account_password_reset_token"),
    re_path(r"^settings/$", SettingsView.as_view(), name="account_settings"),
    re_path(r"^delete/$", DeleteView.as_view(), name="account_delete"),
    re_path(r"^agents/$", AgentList.as_view(), name="agents"),
    re_path(r"^agent/(?P<slug>[-\w]+)/$", AgentDetail.as_view(), name="agent_detail"),
]
