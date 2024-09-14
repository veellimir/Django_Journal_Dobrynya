from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpRequest, HttpResponse

from typing import Dict

from .models import TaskUser
from .forms import TaskUserForm

from users.models import ProfileAdmin


@login_required
def tasks(request: HttpRequest) -> HttpResponse:
    page: str = "user_tasks" if not request.user.is_superuser else "admin_tasks"

    user_tasks: TaskUser = TaskUser.objects.filter(user=request.user) \
        if not request.user.is_superuser else TaskUser.objects.all()

    if request.method == "POST":
        form = TaskUserForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.initiator = ProfileAdmin.objects.get(user=request.user)

            task.save()
            messages.success(request, f"Задача успешно создана")
            return redirect("tasks")
        else:
            messages.error(request, "Что-то пошло не так ")
    else:
        form = TaskUserForm()

    context: Dict[str, object] = {
        "title": "Задачи",
        "user_tasks": user_tasks,
        "page": page,
        "form": form
    }
    return render(request, "tasks/tasks.html", context)


@login_required
def task_details(request: HttpRequest, task_id: int) -> HttpResponse:
    task: TaskUser = get_object_or_404(TaskUser, id=task_id)

    context: Dict[str, object] = {
        "title": f"Задача {task.title}",
        "my_task": task
    }
    return render(request, "tasks/detail_task.html", context)


@login_required
def change_task_status(request: HttpRequest, task_id: int, new_status: int) -> HttpResponse:
    task: TaskUser = get_object_or_404(TaskUser, id=task_id)

    current_status = task.status_task

    if (current_status == TaskUser.NEW_TASK and new_status == TaskUser.WORK_TASK) or \
            (current_status == TaskUser.WORK_TASK and new_status == TaskUser.CHECK_TASK):
        task.status_task = new_status

        task.save()
        if new_status == TaskUser.WORK_TASK:
            messages.success(request, "Задача взята в работу")
        elif new_status == TaskUser.CHECK_TASK:
            messages.success(request, "Задача отправлена на проверку")

        else:
            messages.error(request, "Невозможно изменить статус задачи")

    return redirect("tasks")


@login_required
def confirm_execution_task(request: HttpRequest, task_id: int) -> HttpResponse:
    task: TaskUser = get_object_or_404(TaskUser, id=task_id)

    if request.method == "POST":
        estimation: str = request.POST.get("estimation_task")

        if task.status_task != TaskUser.END_TASK:
            task.estimation_task = estimation
            task.status_task = TaskUser.END_TASK
            task.save()

            if estimation is not None:
                task.user.profile.points += int(estimation)
                task.user.profile.save()

                messages.success(request, "Задача успешно подтверждена")
            else:
                messages.warning(request, "Задача подтверждена, но оценка задачи не установлена")

        return redirect("tasks")


@login_required
def delete_task(request: HttpRequest, task_id: int) -> HttpResponse:
    task: TaskUser = get_object_or_404(TaskUser, id=task_id)

    task.delete()
    messages.success(request, f"Задача {task.title} удалена" )
    return redirect("tasks")