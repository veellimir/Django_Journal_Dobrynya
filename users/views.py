from django.shortcuts import render


def user_login(request):
    page = "login"

    context = {
        "title": "Войти",
        "page": page
    }
    return render(request, "users/login_register.html", context)


def user_register(request):
    page = "register"

    context = {
        "title": "Регистрация",
        "page": page
    }
    return render(request, "users/login_register.html", context)