from django.contrib import admin
from .models import Courses
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
   list_display=('course_name','year')
   list_filter=('year','course_name')
   ordering=('course_name',)



admin.site.register(Courses,CourseAdmin)