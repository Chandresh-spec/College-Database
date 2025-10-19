
from django.urls import path
from . import views


urlpatterns = [
    path('bca/',views.BCA_views,name='bca'),   

]