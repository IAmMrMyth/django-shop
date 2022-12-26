from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm, LoginRequestForm,OTPConfirmForm
from django.contrib.auth import (authenticate, login, logout, get_user_model)
from django.contrib.auth.mixins import (LoginRequiredMixin)
from django.core.cache import cache
from .utiles import send_otp
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


class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


class LoginRequestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/otp_login.html")

    def post(self, request, *args, **kwargs):
        form = LoginRequestForm(request.POST or None)
        if form.is_valid():
            phone = form.cleaned_data.get('phone_number')
            request.session['phone_number'] = phone
            context = send_otp(
                request=request, phone=phone)
            return redirect("accounts:otp_confirm")
        return render(request, "accounts/otp_login.html", {'error_messages': form.errors})


class LoginConfirmView(View):
    def get(self, request, *args, **kwargs):
        phone_number = request.session.get('phone_number')
        if not phone_number:
            return redirect("accounts:otp_login")
        return render(request, "accounts/otp_confirm.html", {"phone_number": phone_number})

    def post(self,request, *args, **kwargs):
        form = OTPConfirmForm(request.POST or None)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            received_code = form.cleaned_data['otp_code']
            otp = cache.get(phone)
            if otp is not None:
                if str(otp) == received_code:
                    cache.delete(phone)
                    cache.delete(f"{phone}-for-authentication")
                    user = get_user_model().objects.filter(phone_number = phone).first()
                    if not user:
                        user = get_user_model().objects.create(phone_number = phone)
                    login(request,user)
                    del request.session['phone_number']
                    return redirect("/")
                else:
                    message = "otp code is incorrect"
            else:
                message = "we dont send you any otp code try again"
        else:
            message = form.errors
            phone = request.session.get('phone_number')
            print(message)
        return render(request,"accounts/otp_confirm.html",{'error_messages':message,'phone_number':phone})