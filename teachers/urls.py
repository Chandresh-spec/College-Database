
from django.urls import path
from . import views


urlpatterns = [
    
   path('all/',views.all_branch_view,name='all'),
   path('teacher/<str:branch>/',views.BBA_teacher_view,name='BBATeacher')

]