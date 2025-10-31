
from django.urls import path
from . import views
from .views import ProfileDetail


urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_views,name='signup'),
    path('logout/',views.logout_views,name='logout'),
    path('profile/',ProfileDetail.as_view(),name='profile'),
    path('edit/',views.edit_profile,name='edit')

]