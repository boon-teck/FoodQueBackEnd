from django.contrib import admin
from tasks.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name_of_task',)
admin.site.register(Task, TaskAdmin)
