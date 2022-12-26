from random import randint
from django.core.cache import cache
from django.conf import settings


def send_sms(phone: str, otp: str):
    pass


def otp_generator() -> str:
    return randint(10000, 100000)


def send_otp(request, phone:str)-> dict:
    otp = otp_generator()
    if cache.get(f"{phone}-for-authentication"):
        return {
            "message": "we cant re-send otp code...",
            "code": -2,
        }

    cache.set(f"{phone}-for-authentication", phone, 60)
    cache.set(phone, otp, settings.EXPIRY_TIME_OTP)
    print(otp)
    # TODO Here the otp code must later be sent to the user's phone number by SMS system.
    # But in debug mode we return the otp code.
    send_sms(phone, otp)

    context = {"message": f"send.", "code": 1}
    return context
