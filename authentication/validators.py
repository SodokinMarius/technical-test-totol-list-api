from django.core.validators import RegexValidator

def usernameValidator():
    
    username_validator = RegexValidator(
        r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$',
        message='Username must contain at least 8 characters, including at least 1 uppercase letter, 1 lowercase letter, and 1 number'
    )
    return username_validator

def passwordValidator():
    password_validator = RegexValidator(
    r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*])(?=.*\d)[A-Za-z\d!@#$%^&*]{8,}$',
    message='Password must contain at least 8 characters, including at least 1 uppercase letter, 1 lowercase letter, 1 special character, and 1 number'
    )
    return password_validator
