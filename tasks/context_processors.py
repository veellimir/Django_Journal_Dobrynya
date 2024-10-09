from django.http import HttpRequest
from typing import Dict

from tasks.models import TaskUser


def quantity_new_task_user(request: HttpRequest) -> Dict[str, int]:
    if request.user.is_authenticated:
        new_tasks_count = TaskUser.objects.filter(user=request.user, status_task=TaskUser.NEW_TASK).count()
        return {'new_tasks_count': new_tasks_count}

    return {'new_tasks_count': 0}


def quantity_check_task_user(request: HttpRequest) -> Dict[str, int]:
    if request.user.is_authenticated and request.user.is_superuser:
        check_tasks_count = TaskUser.objects.filter(status_task=TaskUser.CHECK_TASK).count()
        return {'check_tasks_count': check_tasks_count}

    return {'check_tasks_count': 0}


