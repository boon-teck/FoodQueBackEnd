from django.urls import path
from . import views

urlpatterns = [
    # path('',views.all_messages, name='messages_all'),
    path('create/<uuid:id>',views.create_comment, name='create_comments'),
    # path('edit/<uuid:messageid>',views.edit_task, name='messages_edit'),
    # path('delete/<uuid:messageid>',views.delete_task, name='messages_delete'),
]