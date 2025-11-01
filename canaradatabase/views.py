from django.shortcuts import render,get_object_or_404,redirect
from .models import Student
from django.db.models import  Q
# Create your views here.
from .forms import AddStudent
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.urls import reverse_lazy

from django.core.paginator  import Paginator,EmptyPage,PageNotAnInteger

# class ListStudnet_view(ListView):
    # model=Student
    # template_name='index.html'
    # context_object_name='students'
# 


class StudentPage_view(DetailView):
    model=Student
    template_name='student.html'
    context_object_name='st'





class Student_create_view(CreateView):
    model=Student
    template_name='addstudent.html'
    fields=['name','course_name','gmail','uucms_num','rno','photo']
    success_url=reverse_lazy('home')



class Update_student_view(UpdateView):
    model=Student
    template_name='edit.html'
    fields=['name','course_name','gmail','uucms_num','rno','photo']
    success_url=reverse_lazy('home')




def search_paginator(request):
    query=request.GET.get('q')

    search=Student.objects.filter(Q(name__icontains=query)|Q(rno__icontains=query))

    paginator=Paginator(search,4)

    page_number=request.GET.get('page',1)

    


    try:
        page_obj=paginator.page(page_number)
    
    except PageNotAnInteger:
        page_obj=paginator.page(1)
    
    except EmptyPage:
        page_obj=paginator.page(paginator.num_pages)


    

    context={
        'page_obj':page_obj,
        'paginator':paginator,
        'query':query,

    }
    

    return render(request,'search.html',context)






        
    



def post_list(request):
    post=Student.objects.all()

    paginator=Paginator(post,4)

    page_number=request.GET.get('page',1)


    try:
        page_obj=paginator.page(page_number)

    except PageNotAnInteger:
        page_obj=paginator.page(1)
    
    except EmptyPage:
        page_obj=paginator.page(paginator.num_pages)


    
    context={
        'page_obj':page_obj,
        'paginator':paginator,
    }


    return render(request,'index.html',context)