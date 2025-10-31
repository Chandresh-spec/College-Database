from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from .forms import SignupForm,ProfileForm
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,CreateView,UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# Create your views here.
class Signup_view(CreateView):
    model=User
    form_class=SignupForm
    template_name='accounts/signup.html'
    success_url=reverse_lazy('home')



class CustomLogin_view(LoginView):
    template_name='accounts/login.html'
    redirect_authenticated_user=True





def logout_views(request):
    logout(request)
    return redirect('home')




class ProfileDetail(LoginRequiredMixin,DetailView):
    model=Profile
    template_name='profile.html'
    context_object_name='profile'

    login_url=reverse_lazy('login')


    def get_object(self):
        return self.request.user.profile



class Update_Profile_view(UpdateView):
    model=Profile
    template_name='edit.html'
    fields=['full_name','phone','bio','profile_img','gmail','city']
    success_url=reverse_lazy('profile')

    
    def get_object(self,queryset=None):
        return self.request.user.profile
    