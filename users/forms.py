from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile
from .base_forms import BaseFormUsers


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


class UserProfileForm(BaseFormUsers):
    class Meta:
        model = Profile
        fields = [
            "profile_image",
            "date_of_birth",
            "phone",
            "telegram",
            "whatsapp",
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


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )