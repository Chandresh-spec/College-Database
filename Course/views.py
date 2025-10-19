from django.shortcuts import render
from .models import Courses
# Create your views here.

def BCA_views(request):
    bca_courses=Courses.objects.filter(course_name='BCA')
    return render(request,'bca.html',{'bca_courses':bca_courses})



def BBA_Views(request):
    bba_course=Courses.objects.filter(course_name='BBA')
    return render(request,'bba.html',{'bba_course':bba_course})