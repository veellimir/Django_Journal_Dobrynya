from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import TaskUser


@login_required
def tasks(request):
    user_tasks = TaskUser.objects.filter(user=request.user)

    context = {
        "user_tasks": user_tasks
    }
    return render(request, "tasks/tasks.html", context)

