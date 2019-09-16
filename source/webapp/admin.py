from django.contrib import admin
from webapp.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'specific', 'status', 'date_of_completion']
    list_filter = ['status']
    search_fields = ['description']
    exclude = []


admin.site.register(Task, TaskAdmin)

# Register your models here.
