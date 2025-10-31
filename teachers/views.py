from django.shortcuts import render,get_object_or_404
from .models import Teacher
from Course.models import Courses
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView,DetailView


class Teacher_view(ListView):
    model=Teacher
    template_name='all.html'
    context_object_name='teachers'


    def get_queryset(self):

        branch=self.kwargs.get('branch')

        if  branch and branch.lower()=='all':
            return Teacher.objects.all()
        
        else:
            return Teacher.objects.filter(branch__course_name__iexact=branch)
    


    def get_context_data(self,**kwargs):
            context = super().get_context_data(**kwargs)

            courses=Courses.objects.values_list('course_name',flat=True).distinct()

            context['courses']=sorted(set(courses))

            context['selected_branch']=self.kwargs.get('branch')

            return context
            
            
        
       

        



class Teacher_detail_view(DetailView):
    model=Teacher
    template_name='teacher_detail.html'
    context_object_name='teacher'
    



