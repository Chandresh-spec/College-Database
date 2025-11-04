
from django.urls import path
from . import views
from .views import StudentPage_view,Student_create_view,Update_student_view,Search_List,ListStudnet_view


urlpatterns = [
    path('home/',ListStudnet_view.as_view(),name='home'),
    path('studentinfo/<int:pk>/',StudentPage_view.as_view(),name='studentinfo'),
    path('addstudent/',Student_create_view.as_view(),name='addstudent'),
    path('edit/<int:pk>/',Update_student_view.as_view(),name='edit'),
    path('search/',Search_List.as_view(),name='search')
    

]