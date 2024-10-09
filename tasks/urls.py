from django.urls import path
from . import views


urlpatterns = [
    path("tasks/", views.tasks, name="tasks"),
    path('task-details/<int:task_id>/', views.task_details, name='task_details'),
    path('task-confirm/<int:task_id>/', views.confirm_execution_task, name='task_confirm'),
    path('change-task-status/<int:task_id>/<int:new_status>/', views.change_task_status, name='change_task_status'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),

]