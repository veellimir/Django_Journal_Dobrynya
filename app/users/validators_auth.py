from django.core.exceptions import ValidationError

import re


def validate_username(username: str) -> str:
    if not re.match(r"^[a-z]{3,15}$", username):
        raise ValidationError(
            "Имя пользователя должно быть содержать маленькие буквы, "
            "длиной от 3 до 15 символов, а так же только буквы (Английского алфавита)"
            ""
        )
    return username


def validate_first_name(first_name: str) -> str:
    first_name: str = first_name.capitalize()

    if not re.match(r"^[а-яА-ЯёЁ]{4,20}$", first_name):
        raise ValidationError(
            "Имя может содержать только буквы Русского "
            "алфавита, а так же от 4 до 20 символов"
        )
    return first_name


def validate_last_name(last_name: str) -> str:
    last_name: str = last_name.capitalize()

    if not re.match(r"^[а-яА-ЯёЁ]{4,20}$", last_name):
        raise ValidationError(
            "Фамилия может содержать только буквы Русского "
            "алфавита, а так же от 4 до 20 символов"
        )
    return last_name


def validate_email(email: str) -> str:
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        raise ValidationError("Введите действительный адрес электронной почты.")
    return email


def validate_password(password: str) -> str:
    if len(password) < 8:
        raise ValidationError("Пароль должен быть не менее 8 символов.")
    if not re.search(r"[A-Za-z]", password):
        raise ValidationError("Пароль должен содержать буквы (Английского алфавита).")
    if not re.search(r"\d", password):
        raise ValidationError("Пароль должен содержать хотя бы одну цифру.")
    if not re.search(r"[@$!%*#?&]", password):
        raise ValidationError("Пароль должен содержать хотя бы один из -> @$!%*#?& специальных символов.")
    return password


def validate_telegram(link: str) -> str:
    link: str = link.strip()

    if link.startswith("https://t.me/"):
        return link
    if link.startswith("@"):
        return f"https://t.me/{link[1:]}"
    return f"https://t.me/{link}"