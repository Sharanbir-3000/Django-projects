from django.contrib import admin
from .models import Task

@admin.register(Task)
class CustomerDetail(admin.ModelAdmin):
    list_display = ('task_name','status')