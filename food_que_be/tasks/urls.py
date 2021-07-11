from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.all_tasks, name='tasks_main_page'),
    path('show/<uuid:id>',views.show_task, name='task_show_page'),
    path('create/',views.create_task, name='task_create_page'),
]