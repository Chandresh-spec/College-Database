
from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home,name='home'),
    path('studentinfo/<int:pk>/',views.student_view,name='studentinfo'),
    path('addstudent/',views.add_student_view,name='addstudent'),
    path('edit/<int:pk>/',views.edit_student_view,name='edit'),
    path('search/',views.search_view,name='search')
    

]