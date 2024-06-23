from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .forms import CustomUserRegisterForm, UserProfileForm
from .models import Profile


def user_logout(request):
    logout(request)
    messages.success(request, "Вы вышли.")
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

            if not user.is_superuser:
                try:
                    profile = Profile.objects.get(user=user)
                    return redirect("home")
                except Profile.DoesNotExist:
                    return redirect("questionnaire")
            else:
                return redirect("home")

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
            return redirect("login")
        else:
            for error in form.errors.values():
                messages.error(request, error)
    context = {
        "title": "Регистрация",
        "page": page,
        "form": form,
    }
    return render(request, "users/login_register.html", context)


@login_required
def user_questionnaire(request):
    page = "questionnaire"

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            messages.success(request, "Анкета успешно заполнена")
            return redirect("home")
        else:
            messages.error(request, "Анкета заполнена некорректно, проверьте правильность заполнение полей")
    else:
        form = UserProfileForm(instance=profile)

    context = {
        "title": "Заполни анкету",
        "form": form,
        "page": page
    }
    return render(request, "mainapp/questionnaire.html", context)


@login_required
def all_users(request):
    users = User.objects.all()

    context = {
        "title": "Дружина",
        "users": users
    }
    return render(request, "users/users.html", context)


@login_required
def profile(request, pk):
    prof = get_object_or_404(User, pk=pk)

    context = {
        "title": "Информация о пользователе",
        "prof": prof
    }
    return render(request, "users/profile.html", context)