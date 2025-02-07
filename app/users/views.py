from itertools import chain
from typing import Callable, Dict, List

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from .forms import (
    CustomUserRegisterForm,
    UserProfileForm,
    AdminProfileForm,
    UserParentForm
)
from .models import Profile, ProfileAdmin, ProfileParent
from app.telebot.views import send_message_to_telegram


def superuser_required(view_func: Callable) -> Callable:
    def _wrapped_view_func(request, *args: tuple, **kwargs: dict) -> HttpResponse:
        if not request.user.is_superuser:
            return redirect("home")
        return view_func(request, *args, **kwargs)

    return user_passes_test(lambda u: u.is_authenticated)(_wrapped_view_func)


def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.success(request, "Вы вышли.")
    return redirect("login")


def user_login(request: HttpRequest) -> HttpResponse:
    page: str = "login"

    if request.method == "POST":
        username: str = request.POST["username"]
        password: str = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)

            success_login: str = f"Пользователь {user.get_full_name()} вошёл на сайт. ✅ "
            send_message_to_telegram(request, success_login)

            if not user.is_superuser:
                try:
                    prof = Profile.objects.get(user=user)
                    return redirect("home")
                except Profile.DoesNotExist:
                    try:
                        parent_prof = ProfileParent.objects.get(user=user)
                        return redirect("home")
                    except ProfileParent.DoesNotExist:
                        return redirect("user_select_role")

            else:
                return redirect("home")

        messages.error(request, "Нет доступа, или данные введены некорректно")

    context: Dict[str, str] = {
        "title": "Войти",
        "page": page,
    }
    return render(request, "users/login_register.html", context)


def user_register(request: HttpRequest) -> HttpResponse:
    page: str = "register"
    form: CustomUserRegisterForm = CustomUserRegisterForm()

    if request.method == "POST":
        form = CustomUserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            messages.success(request, f"Аккаунт зарегистрирован, ожидаете решение администратора")
            success_register: str = (f""
                                     f"Пользователь 😎  {user.get_full_name()} зарегистрировался. ✅ "
                                     f"Пожалуйста не забудьте выдать ему нужные права ⚠"
                                     )

            send_message_to_telegram(request, success_register)
            return redirect("login")
        else:
            for error in form.errors.values():
                messages.error(request, error)

    context: Dict[str, CustomUserRegisterForm] = {
        "title": "Регистрация",
        "page": page,
        "form": form,
    }
    return render(request, "users/login_register.html", context)


@login_required
def all_users(request: HttpRequest) -> HttpResponse:
    users: List[User] = User.objects.all()

    context: Dict[str, list[User]] = {
        "title": "Дружина",
        "users": users
    }
    return render(request, "users/users.html", context)


@login_required
def all_coach(request: HttpRequest) -> HttpResponse:
    coaches_with_directions: List[ProfileAdmin] = ProfileAdmin.objects.filter(
        directions__isnull=False
    ).distinct()
    coaches_with_personal: List[ProfileAdmin] = ProfileAdmin.objects.filter(
        directions__isnull=True,
        admin_personal__isnull=False
    ).distinct()

    coaches: List[ProfileAdmin] = list(chain(
        coaches_with_directions,
        coaches_with_personal
    ))

    context: Dict[str, List[ProfileAdmin]] = {
        "title": "Команда нашего центра",
        "coaches": coaches,
    }
    return render(request, "users/all_coach.html", context)


@login_required
def profile(request: HttpRequest, pk: int) -> HttpResponse:
    prof: User = get_object_or_404(User, pk=pk)

    context: Dict[str, User] = {
        "title": "Информация о пользователе",
        "prof": prof,
    }
    return render(request, "users/profile.html", context)


@login_required
def user_select_role(request: HttpRequest) -> HttpResponse:
    return render(request, "users/user_select_role.html")


@login_required
def handle_profile(
        request: HttpRequest,
        profile_models,
        form_users,
        page,
        user_type
) -> HttpResponse:
    try:
        prof = profile_models.objects.get(user=request.user)
    except profile_models.DoesNotExist:
        prof = profile_models(user=request.user)

    if request.method == "POST":
        form = form_users(request.POST, request.FILES, instance=prof)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()

            messages.success(request, "Анкета успешно сохранена !")
            return redirect("home")
        else:
            messages.error(request, "Анкета заполнена некорректно, проверьте правильность заполнение полей")
    else:
        form = form_users(instance=prof)

    context = {
        "title": "Профиль",
        "form": form,
        "profile": prof,
        "page": page,
        "user_type": user_type,
    }
    return render(request, "users/questionnaire.html", context)


@login_required
def user_questionnaire(request: HttpRequest) -> HttpResponse:
    return handle_profile(
        request,
        profile_models=Profile,
        form_users=UserProfileForm,
        page="questionnaire",
        user_type="user"
    )


@login_required
def parent_questionnaire(request: HttpRequest) -> HttpResponse:
    return handle_profile(
        request,
        profile_models=ProfileParent,
        form_users=UserParentForm,
        page="parent_questionnaire",
        user_type="parent"
    )


@login_required
@superuser_required
def edit_admin_profile(request: HttpRequest) -> HttpResponse:
    return handle_profile(
        request,
        profile_models=ProfileAdmin,
        form_users=AdminProfileForm,
        page="edit_admin_profile",
        user_type="admin"
    )


@login_required
def profile_awards(request: HttpRequest) -> HttpRequest:
    context = {
        "title": "Мои Награды"
    }
    return render(request, "users/awards.html", context)


def personal_data(request: HttpRequest) -> HttpResponse:
    return render(request, "users/personal_data.html")
