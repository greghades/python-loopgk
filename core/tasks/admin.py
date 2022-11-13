from django.contrib import admin
from .models import Priority, task

# Register your models here.
admin.site.register(task)
admin.site.register(Priority)