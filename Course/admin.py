from django.contrib import admin
from .models import Courses
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
   list_display=('name','year')
   list_filter=('year','name')
   ordering=('name',)



admin.site.register(Courses,CourseAdmin)