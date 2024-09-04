from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile, ProfileAdmin
from mainapp.base_forms import BaseFormUsers

from users.validators_auth import *


class CustomUserRegisterForm(UserCreationForm, BaseFormUsers):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        return validate_username(username)

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        return validate_first_name(first_name)

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        return validate_last_name(last_name)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return validate_email(email)

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        return validate_password(password1)


class UserProfileForm(BaseFormUsers):
    class Meta:
        model = Profile
        fields = [
            "profile_image",
            "date_of_birth",
            "phone",
            "telegram",
            "vk",
            "address",
            "fio_parents",
            "parents_place_work",
            "educational_institution",
            "time_school",
            "outside_club",
            "hobby",
            "sports",
            "about_club",
            "goals_season",
            "participation_competition",
            "wishes"
        ]


class AdminProfileForm(BaseFormUsers):
    class Meta:
        model = ProfileAdmin
        fields = [
            "profile_image",
            "name",
            "surname",
            "patronymic",
            # "directions",
            "phone",
            "telegram",
            "vk",
        ]


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    new_password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )