from django.contrib import admin
from .models import Task
# Register your models here.

class check(admin.ModelAdmin):
    list_display=('mission','status','date_created','date_updated')


admin.site.register(Task,check)
