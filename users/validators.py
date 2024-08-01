from django.core.exceptions import ValidationError

import re


def validate_username(username):
    if not re.match(r"^[a-z]{3,15}$", username):
        raise ValidationError(
            "Имя пользователя должно быть в нижнем регистре, "
            "длиной от 3 до 15 символов и может содержать только"
            " Латинские буквы."
        )
    return username


def validate_first_name(first_name):
    first_name = first_name.lower()

    if not re.match(r"^[а-яА-ЯёЁ]{4,20}$", first_name):
        raise ValidationError(
            "Имя может содержать только буквы Русского "
            "алфавита, а так же от 4 до 20 символов"
        )
    return first_name


def validate_last_name(last_name):
    last_name = last_name.lower()

    if not re.match(r"^[а-яА-ЯёЁ]{4,20}$", last_name):
        raise ValidationError(
            "Фамилия может содержать только буквы Русского "
            "алфавита, а так же от 4 до 20 символов"
        )
    return last_name


def validate_email(email):
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        raise ValidationError("Введите действительный адрес электронной почты.")
    return email


def validate_password(password):
    if len(password) < 8:
        raise ValidationError("Пароль должен быть не менее 8 символов.")
    if not re.search(r"[A-Za-z]", password):
        raise ValidationError("Пароль должен содержать буквы (Английского алфавита).")
    if not re.search(r"\d", password):
        raise ValidationError("Пароль должен содержать хотя бы одну цифру.")
    if not re.search(r"[@$!%*#?&]", password):
        raise ValidationError("Пароль должен содержать хотя бы один специальный символ.")
    return password
