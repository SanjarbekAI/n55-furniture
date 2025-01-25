import threading

from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect
from django.views.generic import FormView

from app_users.forms import RegisterForm, LoginForm
from app_users.utils import send_email_confirmation

UserModel = get_user_model()


class LoginFormView(FormView):
    template_name = 'auth/user-login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        login(request=self.request, user=form.cleaned_data["user"])
        messages.success(self.request, "Please, confirm your email and login")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class RegisterView(FormView):
    template_name = 'auth/user-register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        email_thread = threading.Thread(target=send_email_confirmation, args=(user, self.request,))
        email_thread.start()

        messages.success(self.request, "Please, confirm your email and login")

        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


def confirm_email(request, uid, token):
    try:
        user = UserModel.objects.get(id=uid)
    except UserModel.DoesNotExist:
        return redirect('users:login')

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your email address is verified!")
        return redirect('/')
    else:
        messages.success(request, "Link is not correct")
        return redirect('/')

# class VerifyEmailView(View):
#     def get(self, uid, token):
#         try:
#             user = UserModel.objects.get(id=uid)
#         except UserModel.DoesNotExist:
#             return redirect('users:login')
#
#         if default_token_generator.check_token(user, token):
#             user.is_active = True
#             user.save()
#             messages.success(self.request, "Your email address is verified!")
#             return redirect('/')
#         else:
#             messages.success(self.request, "Link is not correct")
#             return redirect('/')
