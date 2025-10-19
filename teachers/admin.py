from django.contrib import admin
from .models import Teacher

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    search_fields=['t_name']
    ordering = ['experience']
    list_filter = ['branch']




admin.site.register(Teacher,TeacherAdmin)