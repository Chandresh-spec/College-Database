from django.shortcuts import render,get_object_or_404
from .models import Student
# Create your views here.


def home(request):
    students=Student.objects.all()
    return render(request, 'index.html',{'students':students})



def student_view(request,pk):
    st=get_object_or_404(Student,pk=pk)

    return render(request,'student.html',{'st':st})