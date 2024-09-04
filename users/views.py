from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.models import User

from .forms import CustomUserRegisterForm, UserProfileForm, AdminProfileForm
from .models import Profile, ProfileAdmin


def superuser_required(view_func):
    # TODO: banning ordinary users

    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return user_passes_test(lambda u: u.is_authenticated)(_wrapped_view_func)


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

            if not user.is_superuser:
                try:
                    prof = Profile.objects.get(user=user)
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
def all_users(request):
    users = User.objects.all()

    context = {
        "title": "Дружина",
        "users": users
    }
    return render(request, "users/users.html", context)


@login_required
def all_coach(request):
    coaches = ProfileAdmin.objects.all()

    context = {
        "title": "Тренерский состав",
        "coaches": coaches,
    }
    return render(request, "users/all_coach.html", context)


@login_required
def profile(request, pk):
    prof = get_object_or_404(User, pk=pk)

    context = {
        "title": "Информация о пользователе",
        "prof": prof
    }
    return render(request, "users/profile.html", context)


@login_required
def handle_profile(request, profile_models, form_users, page):
    """
    Function profile data
    :param request:
    :param profile_models:
    :param form_users:
    :param page:
    :return:
    """
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
    }
    return render(request, "users/questionnaire.html", context)


@login_required
def user_questionnaire(request):
    # TODO: questionnaire users

    return handle_profile(
        request,
        profile_models=Profile,
        form_users=UserProfileForm,
        page="user_questionnaire"
    )


@login_required
@superuser_required
def edit_admin_profile(request):
    # TODO: questionnaire admin

    return handle_profile(
        request,
        profile_models=ProfileAdmin,
        form_users=AdminProfileForm,
        page="edit_admin_profile"
    )


def personal_data(request):
    return render(request, "users/personal_data.html")