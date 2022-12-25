from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm,RegisterForm
from django.contrib.auth import (authenticate, login, logout,get_user_model)
from django.contrib.auth.mixins import (LoginRequiredMixin)
# Create your views here.


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/login.html", {})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['phone_number'], password=data['password'])
            if user != None:
                login(request, user)

                return redirect("/")
            else:
                return render(request, "accounts/login.html", {'error_messages': "phone number or password is incorrect"})

        return render(request, "accounts/login.html", {'error_messages': form.errors})

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/register.html")
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            data.pop('password2')
            user = get_user_model().objects.create_user(**data)
            login(request, user)
            return redirect('/')
        return render(request, "accounts/register.html", {'error_messages': form.errors})

class LogoutView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")
