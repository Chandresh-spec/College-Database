from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from .forms import SignupForm,ProfileForm
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.urls import reverse_lazy
# Create your views here.

def signup_views(request):
    if request.method=='POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request,user)
            return  redirect('home')
        
        return render(request,'accounts/signup.html',{'form':form})
    

    else:
        form=SignupForm()
        return render(request,'accounts/signup.html',{'form':form})
    



def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():

            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')


            user=authenticate(username=username,password=password)


            if user:
                login(request,user)
                return redirect('home')
        return render(request,'accounts/login.html',{'form':form})
    

    else:
        form=AuthenticationForm()
    
    return render(request,'accounts/login.html',{'form':form})




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


@login_required
def edit_profile(request):
    profile=request.user.profile
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile')
        
        return render(request,'edit.html',{'form':form})
    

    else:
        form=ProfileForm(instance=profile)
    return render(request,'edit.html',{'form':form})