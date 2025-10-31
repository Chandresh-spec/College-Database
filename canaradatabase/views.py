from django.shortcuts import render,get_object_or_404,redirect
from .models import Student
from django.db.models import  Q
# Create your views here.
from .forms import AddStudent
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.urls import reverse_lazy

class ListStudnet_view(ListView):
    model=Student
    template_name='index.html'
    context_object_name='students'



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





class Search_Students(ListView):
    model=Student
    template_name='search.html'
    context_object_name='students'



    def get_queryset(self):
        query=self.request.GET.get('q')

        if query:
            return Student.objects.filter(Q(name__icontains=query) |Q(rno__icontains=query))
        
        return Student.objects.all()