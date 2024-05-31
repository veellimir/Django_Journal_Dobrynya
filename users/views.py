from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import CustomUserRegisterForm, UserProfileForm
from .models import Profile


def user_logout(request):
    logout(request)
    return redirect("login")


def user_login(request):
    page = "login"

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f"Здравствуйте, {user.username}")

            try:
                profile = Profile.objects.get(user=user)
                return redirect("home")
            except Profile.DoesNotExist:
                return redirect("questionnaire")

        messages.error(request, "Нет доступа, или данные введены некорректно")

    context = {
        "title": "Войти",
        "page": page,
    }
    return render(request, "users/login_register.html", context)


def user_register(request):
    page = "register"
    form = CustomUserRegisterForm()

    if request.method == "POST":
        form = CustomUserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            messages.success(request, f"Аккаунт зарегистрирован, ожидаете решение администратора")
        else:
            messages.error(request, "ошибка")

    context = {
        "title": "Регистрация",
        "page": page,
        "form": form,
    }
    return render(request, "users/login_register.html", context)


@login_required
def user_questionnaire(request):
    form = UserProfileForm(request.POST)

    context = {
        "title": "Заполни анкету",
        "form": form
    }
    return render(request, "mainapp/questionnaire.html", context)