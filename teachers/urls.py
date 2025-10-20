
from django.urls import path
from . import views


urlpatterns = [
   path('teacher/<str:branch>/',views.teacher_view,name='Teacher'),
   path('detail/<int:pk>/',views.teacher_detail_view,name='detail'),

]