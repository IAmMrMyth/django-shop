from django.urls import path
from .views import LoginView, LogoutView, RegisterView, LoginRequestView, LoginConfirmView

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("otp/login/", LoginRequestView.as_view(), name="otp_login"),
    path("otp/confirm/", LoginConfirmView.as_view(), name="otp_confirm"),

    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),

]
