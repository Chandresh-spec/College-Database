
from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_views,name='signup'),
    path('logout/',views.logout_views,name='logout'),
    path('profile/',views.profile_view,name='profile'),

]