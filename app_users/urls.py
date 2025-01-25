from django.urls import path

from app_users.views import RegisterView, confirm_email, LoginFormView, AccountUpdateView, PasswordUpdateView

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginFormView.as_view(), name="login"),
    # path("logout/", RegisterView.as_view(), name="register"),
    path("account/", AccountUpdateView.as_view(), name="account"),
    path("update/password/", PasswordUpdateView.as_view(), name="update-password"),
    # path("forget/password/", RegisterView.as_view(), name="register"),
    # path("verification/resend/", RegisterView.as_view(), name="register"),
    path("verification/<int:uid>/<str:token>/", confirm_email, name="confirm-email"),
]
