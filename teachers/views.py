from django.shortcuts import render
from .models import Teacher
# Create your views here.

def all_branch_view(request):
   items=Teacher.objects.all()
   return render(request,'all.html',{'items':items})



def Bca_teacher_view(request):
   items=Teacher.objects.filter(branc='bcm')
   return render(request,'bca.html',{'items':items})

def BBA_teacher_view(request,branch):
   items=Teacher.objects.filter(branch=branch)
   return render(request,'bba.html',{'items':items})


