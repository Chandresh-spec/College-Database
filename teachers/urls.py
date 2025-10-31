
from django.urls import path
from . import views
from .views import Teacher_detail_view,Teacher_view

urlpatterns = [
   path('teacher/<str:branch>/',Teacher_view.as_view(),name='Teacher'),
   path('detail/<int:pk>/',Teacher_detail_view.as_view(),name='detail'),

]