from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(
    regex="^[0-9]{11}$",
    message="شماره وارد شده اشتباه است."
)