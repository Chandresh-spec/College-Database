from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignupForm
# Create your views here.

def signup_views(request):
    if request.method=='POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request,user)
            return  redirect('home')
        
        return render(request,'signup.html',{'form':form})
    

    else:
        form=SignupForm()
        return render(request,'signup.html',{'form':form})
    



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
        return render(request,'login.html',{'form':form})
    

    else:
        form=AuthenticationForm()
    
    return render(request,'login.html',{'form':form})




def logout_views(request):
    logout(request)
    return redirect('home')

