from django.shortcuts import render
from .models import Courses
# Create your views here.


def BCA_views(request):
    return render(request,'bca.html')



def BBA_Views(request):
    return render(request,'bba.html')