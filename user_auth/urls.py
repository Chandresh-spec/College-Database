
from django.urls import path
from . import views
from .views import ProfileDetail
from .views import Signup_view,CustomLogin_view,Update_Profile_view
urlpatterns = [
    path('login/',CustomLogin_view.as_view(),name='login'),
    path('signup/',Signup_view.as_view(),name='signup'),
    path('logout/',views.logout_views,name='logout'),
    path('profile/',ProfileDetail.as_view(),name='profile'),
    path('edit/',Update_Profile_view.as_view(),name='edit')

]